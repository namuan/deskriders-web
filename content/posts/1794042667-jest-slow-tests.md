+++ 
date = 2026-11-07T09:11:08Z
title = "Diagnosing Slow Jest Tests: Timings, Memory, and CI Regressions"
description = "A practical guide to finding slow Jest tests, investigating startup overhead and memory growth, and tracking performance regressions in CI."
slug = "diagnosing-slow-jest-tests"
tags = ["jest", "testing", "javascript", "performance", "ci"]
categories = ["Engineering"]
externalLink = ""
series = []
+++

A unit test suite usually gets slower gradually: another shared setup import, another real timer, another expensive fixture. Eventually, running tests becomes something you postpone.

The useful starting point is measurement. Find out whether the extra time belongs to individual tests, test-file startup, resource contention, or work that remains after assertions finish. Each points to a different investigation.

This guide builds a small diagnostic workflow using Jest's built-in options, a timing-report script, and Node's CPU profiler. Examples assume Jest is installed locally and commands run from the project root. Check `npx jest --version` and the documentation for your installed version before adopting options. The linked Jest documentation currently describes version 30.5.

## 1. Make slow test files visible

Merge these options into your existing configuration; preserve your project's environment, transforms, and other settings:

```js
// jest.config.cjs
module.exports = {
  // ...existing configuration
  verbose: true,
  slowTestThreshold: 1,
};
```

`verbose` expands individual test results. `slowTestThreshold` is measured in **seconds** and highlights slow test-file runs in the default reporter. Its default is five seconds. It is a reporting threshold, not a performance assertion: crossing it does not fail the run.

Do not confuse it with `testTimeout`, which limits how long a test may take before failing. Increasing a timeout can accommodate intentionally long work, but does not explain a regression. See the [Jest configuration reference](https://jestjs.io/docs/configuration#slowtestthreshold-number).

One second is a starting point, not a universal budget. Choose a threshold that makes outliers visible in your own suite.

## 2. Separate diagnosis from normal execution

Use two measurements:

- **Normal execution:** the exact command developers or CI use. This measures the experience you want to improve.
- **Diagnostic execution:** a controlled serial run that makes it easier to attribute time to a file.

Capture a diagnostic report:

```bash
npx jest --runInBand --coverage=false --watch=false --json --outputFile=jest-timings.json
```

Here, `--runInBand` runs files in one process, while `--json` and `--outputFile` save machine-readable results. Jest sends other output to stderr in JSON mode. See the [CLI reference](https://jestjs.io/docs/cli).

Serial execution reduces competition between Jest workers, but changes the workload. A serial speedup does not automatically mean your normal parallel run improved. Also, `test.concurrent` can still introduce concurrency within a file.

Turning coverage off helps investigate execution without instrumentation. If your regression happens with coverage enabled, capture a second report with coverage enabled and compare like with like.

For repeatable measurements:

1. Keep Node, Jest, dependencies, machine resources, and worker settings fixed.
2. Separate cold-cache and warm-cache experiments. Do not clear the cache between only some samples.
3. Run one warm-up, then collect at least three to five measured runs.
4. Compare medians and inspect variation.
5. Record the commit and whether coverage was enabled.

Avoid timing while unrelated builds or other heavy processes compete for resources.

## 3. Rank slow files and individual tests

Save the following as `scripts/jest-timings.cjs`. The `.cjs` extension also works in projects using `"type": "module"`.

```js
const fs = require('node:fs');
const path = require('node:path');

const filename = process.argv[2] || 'jest-timings.json';
const report = JSON.parse(fs.readFileSync(filename, 'utf8'));

if (!Array.isArray(report.testResults)) {
  throw new Error('Expected a Jest JSON results file');
}

const relative = filename => path.relative(process.cwd(), filename);
const suites = [];
const tests = [];

for (const suite of report.testResults) {
  const file = relative(suite.name);
  const assertions = suite.assertionResults || [];
  const timed = assertions.filter(test => Number.isFinite(test.duration));

  const elapsed = Number.isFinite(suite.startTime) &&
    Number.isFinite(suite.endTime)
    ? suite.endTime - suite.startTime
    : null;

  suites.push({
    file,
    fileMs: elapsed,
    summedTestMs: timed.reduce((sum, test) => sum + test.duration, 0),
    timedTests: timed.length,
  });

  for (const test of timed) {
    tests.push({ ms: test.duration, test: test.fullName, file });
  }
}

console.log('\nSlowest files');
console.table(suites.sort((a, b) =>
  (b.fileMs ?? -1) - (a.fileMs ?? -1)
).slice(0, 20));

console.log('\nSlowest individual tests');
console.table(tests.sort((a, b) => b.ms - a.ms).slice(0, 20));
```

Run it against any saved report:

```bash
node scripts/jest-timings.cjs jest-timings.json
```

The script uses the CLI JSON structure, including `assertionResults` and individual durations in milliseconds. Do not substitute the differently shaped object passed to a custom reporter or `testResultsProcessor`. Confirm the fields when changing Jest versions; absent timings are skipped rather than treated as zero.

### Interpret the two rankings together

A file taking eight seconds with one test taking seven seconds suggests a different problem from an eight-second file containing dozens of very short tests.

For the first, inspect the slow test and its hooks. For the second, investigate module imports, transforms, environment initialization, shared setup, and suite-level hooks.

Do not label `fileMs - summedTestMs` as exact startup time. The clocks cover different scopes, hooks may contribute differently, and concurrent tests can overlap. Use the gap as a lead, then measure suspected phases directly.

## 4. Isolate the slow test

Run the exact file, then narrow by test name:

```bash
npx jest --runTestsByPath src/example.test.js --runInBand --coverage=false
npx jest --runTestsByPath src/example.test.js --runInBand --coverage=false -t 'returns cached results'
```

`-t` matches a regular expression against the full test name, including surrounding `describe` names. Narrowing the tests does not avoid loading the file and its imports.

Inspect these common suspects:

| Suspect | What to investigate |
| --- | --- |
| Real timers | Debounce delays, retry backoff, polling, or sleeps that could be controlled explicitly |
| External I/O | Accidental network calls, database access, filesystem work, or subprocesses |
| Expensive hooks | Fixture generation or repeated initialization in `beforeEach` |
| Large inputs | Unnecessarily large fixtures, snapshots, or repeated parsing |
| Repeated work | The same expensive setup performed for every case |
| Console output | Large logs or repeated warnings |

Measure suspected operations with `performance.now()` or temporary timers. Remove diagnostic logging before comparing final timings.

Fake timers can help test time-dependent behavior, but adopt them deliberately: advance the clock, await asynchronous work, and restore timer state. Likewise, mock an external boundary when the test's purpose is local behavior; keep separate coverage for the real integration.

## 5. Investigate slow file startup

When test bodies are fast but files are slow, inspect what runs before them:

- Does a small test import an application entry point or a barrel file that loads many modules?
- Do global setup files initialize services every file does not need?
- Does each file load a large fixture at module scope?
- Are transforms doing unnecessary work?
- Does a test requiring only Node APIs use a browser environment unnecessarily?

Try one change at a time, rerun the same file, and then rerun the full suite. Narrower imports and smaller setup modules can help, but preserve behavior and isolation.

For a controlled cache experiment, use `--no-cache` consistently across samples. Expect a different workload from normal cached execution; do not make it the default profiling command.

## 6. Check memory when later files get slower

If performance degrades as the run progresses, inspect heap usage:

```bash
node --expose-gc ./node_modules/jest/bin/jest.js --runInBand --logHeapUsage --coverage=false
```

This assumes a conventional `node_modules` installation. Adapt the executable path for other package layouts.

Jest recommends combining `--logHeapUsage`, `--runInBand`, and Node's `--expose-gc` option. Treat the result as a trend across test files, not an allocation trace for each assertion. See the [heap usage option](https://jestjs.io/docs/cli#--logheapusage).

A steadily rising heap is a reason to investigate retained objects, caches, listeners, timers, and large fixtures. It is not proof of a leak: module caching and different file workloads can also increase memory. Repeat the experiment and correlate growth with particular files.

For worker-based runs, Jest's `workerIdleMemoryLimit` can recycle workers that exceed a configured memory threshold. Treat that as an operational mitigation; it does not identify the retained objects, and worker restarts have a cost. It is not useful for recycling workers in the serial command above.

## 7. Diagnose hangs separately

If assertions finish but Jest does not exit:

```bash
npx jest --detectOpenHandles
```

This diagnostic attempts to identify resources preventing exit, such as servers, sockets, or timers. It implies serial execution and adds overhead, so do not use its timings as a performance baseline. See [Jest's open-handle diagnostic](https://jestjs.io/docs/cli#--detectopenhandles).

Close resources in appropriate teardown hooks and await asynchronous cleanup. Avoid making `--forceExit` the routine fix: it can conceal unfinished cleanup.

## 8. Compare worker counts in CI

If local runs are fine but CI slows down, test whether the runner is overloaded:

```bash
npx jest --maxWorkers=2
npx jest --maxWorkers=50%
```

Run these as separate experiments with otherwise identical settings. Do not combine `--maxWorkers` with `--runInBand`.

More workers can increase memory use and competition for CPU or shared services. Fewer workers can reduce contention but also reduce parallelism. Choose based on repeated wall-clock measurements on the actual CI runner.

`maxWorkers` controls the worker pool. `maxConcurrency` controls concurrency for `test.concurrent`; they solve different problems.

## 9. Capture a CPU profile when timings are insufficient

For CPU-heavy cases, profile an isolated file:

```bash
node --cpu-prof --cpu-prof-dir=. ./node_modules/jest/bin/jest.js --runInBand --runTestsByPath src/example.test.js --coverage=false
```

Node writes a `.cpuprofile` file when the process exits. Load it into a compatible CPU profile viewer, such as Chrome DevTools' JavaScript Profiler. Node documents the options in its [command-line reference](https://nodejs.org/api/cli.html#--cpu-prof).

Inspect where samples accumulate: application code, fixture construction, serialization, transformation, or garbage collection. A CPU profile helps explain active CPU time; a slow test waiting on network I/O may require separate instrumentation around the awaited operation.

Profiling adds overhead. Use the profile to locate work, then verify improvements with ordinary timing runs.

## 10. Track regressions in CI

A static slow threshold will not catch a test growing from 100 ms to 400 ms. Historical comparison is a separate step.

A practical rollout is:

1. Save timing JSON as a CI artifact alongside commit and environment metadata.
2. Establish a baseline from several runs on the main branch.
3. Match tests by repository-relative file path and full test name. Include project identity in multi-project repositories.
4. Compare medians for matching tests and files.
5. Report new or renamed tests separately.
6. Start with warnings; enforce budgets after measuring normal variation.

An illustrative starting rule is to flag a test when its median duration increases by **both more than 25% and more than 100 ms**:

```js
function isRegression(baselineMs, currentMs) {
  return currentMs - baselineMs > 100 &&
    currentMs > baselineMs * 1.25;
}
```

These thresholds are a suggested policy, not a Jest feature or a universal standard. Tune them to your runner and workload. Missing timings must remain missing; failed or incomplete runs should not silently become valid performance baselines.

Track total wall-clock time as well. Individual tests can remain stable while imports get more expensive, worker contention increases, or the suite simply adds more tests. For tests intentionally executed concurrently, avoid treating the sum of durations as elapsed time.

## A compact troubleshooting reference

| Observation | First investigation |
| --- | --- |
| One assertion is consistently slow | Its body, hooks, timers, retries, and I/O |
| File is slow; assertions are fast | Imports, transforms, environment, and setup |
| Later files get progressively slower | Heap growth and retained state |
| Assertions finish but the process stays alive | Open handles and teardown |
| Parallel CI runs are disproportionately slow | Worker count, memory pressure, and shared resources |
| Timings vary widely between runs | Runner load, cache state, external dependencies, and sample size |

Start with the normal run, capture a controlled timing report, isolate the outlier, and investigate the resource it consumes. After changing the code or configuration, verify both the isolated case and the command your team actually runs.

## References

- [Jest CLI options](https://jestjs.io/docs/cli)
- [Jest configuration](https://jestjs.io/docs/configuration)
- [Node.js command-line options](https://nodejs.org/api/cli.html)

Documentation reviewed on November 7, 2026. Use the version selector in Jest's documentation when working with an older release.
