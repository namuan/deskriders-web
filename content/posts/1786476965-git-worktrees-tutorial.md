+++ 
date = 2026-08-11T20:36:06+01:00
title = "Git Worktrees: Multiple Trees, One Repository"
description = "Stop cloning. Stop stashing. Start branching in parallel. A practical guide to git worktrees — the workflow that lets you run hotfixes, parallel builds, and long-running test suites in separate working directories without ever losing context."
slug = "git-worktrees-tutorial" 
tags = ["git", "worktrees", "developer-tools", "workflow", "cli"]
categories = ["development"]
externalLink = ""
series = []
+++

Stop cloning. Stop stashing. Start branching in parallel.

Git worktrees give you a second (or third, or tenth) working directory attached to a single repository — the same `.git`, the same object database, the same refs — but with an independent working tree, HEAD, and index. One repo, many folders. One `.git`, many trees.

---

## The Problem — One Working Tree Is a Bottleneck

You're 200 lines deep into a feature branch when a critical bug ships to prod. The fix needs `main` — but you can't lose your seat. Your IDE indexes are warm, your tests are mid-run, your terminal is full of context.

Here are the classic escapes, and why each one hurts:

- **`git stash`** — Shelves your work, but the mental model vanishes with it. Stashes get lost, conflict on pop, and you still can't run the fix alongside your in-progress branch.
- **`git clone . ../hotfix`** — A second full repo. New remote, new refs, new disk. Submodules, hooks, and config all diverge. You'll spend the next hour syncing them back.
- **`git checkout main`** — Flips the only working tree you have. Build artifacts wiped, IDE indexes rebuilt, terminal context lost. Re-checking out the feature later feels like a reboot.

`git worktree add ../hotfix main` — the better way →

---

## What Is a Worktree?

An extra working directory linked to the same repository. It checks out a different branch but shares the same `.git` directory, the same object database, the same refs, remotes, and config.

```
myproject/                    ← main worktree (.git lives here)
├── .git/                     ← shared object DB + refs
└── ../myproject-hotfix/      ← worktree #2 [hotfix/y]
└── ../myproject-feature/     ← worktree #3 [feature/x]
└── ../myproject-review/      ← worktree #4 [review/pr-42]

# each worktree has its own: working files, HEAD + index,
# build artifacts (node_modules/, target/)
```

Key properties:

- **Shared object database** — Every worktree reads from the same object database. No duplicated history, no separate remotes to keep in sync.
- **Independent HEAD + index** — Each worktree has its own HEAD, index, and staged changes. Branches can be checked out in parallel.
- **Disk-efficient** — Only the working files are duplicated. Git objects, packs, and deltas are shared across every worktree.
- **Branches are exclusive** — A branch checked out in one worktree cannot be checked out in another — this prevents index races.

## Worktree vs Branch vs Clone vs Stash

Each tool solves a different problem. Pick by what you need to keep separate.

| Aspect | Git Worktree | Git Branch | Git Clone | Git Stash |
|---|---|---|---|---|
| Shares single `.git` database? | yes | yes | no | yes |
| Independent working directory? | yes | no | yes | no |
| Independent HEAD / index? | yes | no | yes | no |
| Disk cost | working files only | none | full repo copy | a diff blob |
| Network sync needed? | no | no | yes | no |
| Survives reboot / terminal close? | yes | yes | yes | no (unless pushed) |
| Best for | parallel long-running builds, hotfixes | switching intent in one tree | forks, separate remotes | quick interruptions under 5 min |

**Rule of thumb:** stash < 5 min · branch for switching · clone for forks/experiments · worktree for parallel work that needs to keep running.

---

## Core Commands

Seven subcommands. That's the whole surface area.

```bash
# 1. add — create a worktree checking out an existing branch
$ git worktree add ../hotfix main

# 2. add -b — create a NEW branch in a NEW worktree
$ git worktree add -b feature/x ../feature-x

# 3. list — show every linked worktree
$ git worktree list

# 4. remove — delete a worktree (refuses if dirty)
$ git worktree remove ../hotfix

# 5. prune — clean up metadata for deleted worktrees
$ git worktree prune

# 6. move — relocate a worktree on disk
$ git worktree move ../old-path ../new-path

# 7. lock / unlock — protect from auto-prune (e.g. USB drives)
```

- **Fast** — No clone, no fetch. Sub-second for small repos.
- **Shared** — Object DB is reused. Only working files are new.
- **Prunable** — Stale worktrees self-clean with `git worktree prune`.

---

## Use Case 1 — Hotfix Mid-Review

Ship a prod fix without losing your PR review context.

**Scenario:** You're 40 minutes into reviewing a teammate's PR — test branches spun up, scratch notes in your editor, a half-finished review comment. Then a critical bug hits prod. You need `main`, fast. Stashing risks your review state. Cloning takes minutes. Worktrees let you context-switch in under a second.

```bash
# You are mid-review on ../review/pr-42
$ cd ~/src/myproject

# Spawn a hotfix worktree on main — instant
$ git worktree add ../hotfix main
Preparing worktree (checking out 'main')
HEAD is now at 4f2a1c8 release: v3.2.1

# Step into the hotfix, fix, ship
$ cd ../hotfix
$ git switch -c hotfix/prod-401
$ $EDITOR src/auth/middleware.ts
$ git commit -am "fix: redirect loop on expired session"
$ git push origin hotfix/prod-401

# Return — review state preserved
$ cd -
# ↑ back in ../review/pr-42, comment draft still open
```

**Why it works:**

- Instant checkout — no clone, no fetch, no rebuild of the `.git` directory.
- Review worktree untouched — your editor, terminal, and in-progress comment stay exactly where you left them.
- Fix, push, return — `cd -` and you're back in the review.

**Cost:** 1 sub-second command. **Benefit:** zero context loss.

---

## Use Case 2 — Parallel Builds, Parallel Features

Run tests in one worktree while you keep editing in another.

**Scenario:** You're juggling two features. Each has its own 90-second install, its own test runner, its own dev server. Switching branches in one tree means killing one build to start another — and reinstalling every time. Worktrees give each feature its own `node_modules/`, its own `target/`, its own dev server. Both keep running. You switch terminals, not branches.

```bash
# Two features, two long builds — do not serialize them
$ git worktree add -b feature/auth ../auth
Preparing worktree (new branch 'feature/auth')

$ git worktree add -b feature/ui ../ui
Preparing worktree (new branch 'feature/ui')

# Kick off the auth test suite in its own worktree
$ cd ../auth
$ pnpm install && pnpm test --watch
✓ test/auth.spec.ts (124 tests)

# While that runs, switch to UI work — separate terminal, separate tree
$ cd ../ui
$ pnpm install && pnpm dev
VITE v5.0.0 ready in 412 ms

# Both keep running. No re-install. No re-build.
$ git worktree list
/home/z/src/myproject   4f2a1c8 [main]
/home/z/src/auth        7b9d0e2 [feature/auth]
```

**Why it works:**

- Per-worktree builds — `node_modules/`, `target/`, `build/` live independently. No re-installs.
- Long tests survive — a context switch is just another terminal, not a killed process.
- One window per tree — each worktree is a separate editor window, no tab confusion.

> Serialization is the silent productivity tax. Worktrees remove it.

---

## Recommended Layout & Daily Flow

A convention that scales from solo to team.

```
~/src/
├── myproject/                      # main worktree → main
├── myproject-feature-auth/         # worktree → feature/auth
├── myproject-feature-ui/           # worktree → feature/ui
├── myproject-hotfix-401/           # worktree → hotfix/prod-401
├── myproject-review-pr42/          # worktree → review/pr-42
└── myproject-experiment/           # worktree → experiment/*

# Naming convention: <repo>-<scope>-<ticket>
# • main worktree keeps the bare repo name
# • siblings live one directory up (../<repo>-<scope>)
# • one branch per worktree, never shared
```

**Daily flow:**

1. `git worktree add -b <branch> ../<repo>-<scope>`
2. `cd ../<repo>-<scope>` and work normally
3. Push, open PR, get review
4. `git worktree remove ../<repo>-<scope>` after merge

**Cleanup habit:** Run `git worktree prune` monthly to drop stale metadata. Combine with `git branch --merged | xargs git branch -d` for merged branches.

**One rule:** Never check out the same branch in two worktrees — Git will refuse, and that refusal is the safety net.

---

## Pitfalls to Watch For

Worktrees are great. These four gotchas are the tax — all knowable.

**01. Submodules**

Each worktree checks out submodules independently — they do not share submodule working files.

*Fix:* `git submodule update --init --recursive`

**02. IDE indexes**

JetBrains and VS Code rebuild indexes per worktree. On large monorepos, this is multiple GB and minutes of CPU.

*Fix:* share settings via `.idea/workspace.xml` / project settings

**03. Disk space**

Build artifacts — `node_modules/`, `target/`, `build/` — are per-worktree. Ten worktrees = ten installs.

*Fix:* `git worktree add --no-checkout ../wt && git sparse-checkout init`

**04. Branch locks**

A branch checked out in one worktree cannot be checked out in another. Git refuses — but the error message is opaque.

*Fix:* `git worktree list` to see who has the branch

None of these are blockers. All of them are knowable. Plan ahead.

---

## Tooling That Plays Nice

Worktrees are a Git primitive. These tools make them feel native.

| Tool | Behavior | Command |
|---|---|---|
| **VS Code** | Treats each worktree as its own workspace window with that tree's `.vscode/` settings | `code ../myproject-hotfix` |
| **JetBrains** | Open Project per worktree. Share run configs and inspection profiles via `.idea/runConfigurations/` | File ▸ Open ▸ `../myproject-feature` |
| **zsh / bash aliases** | Three-letter aliases turn the most common worktree ops into muscle memory | `alias gwa="git worktree add" gwls="git worktree list"` |
| **tmux** | One session per worktree. Switch with one keystroke — terminals, editor, and tests stay live | `tmux new -s auth && tmux switch-client -t ui` |
| **Wrappers** (`gw`, `git-worktree-wrapper`) | Opinionated CLIs that bake in the naming + cleanup conventions | `npx gw create feature/auth` |
| **Magit / lazygit** | First-class worktree UIs in the editor. Add, list, remove without leaving the client | lazygit ▸ Worktrees ▸ n |

You don't need any of these. But once you try them, you won't go back.

---

## Cheat Sheet

Print this. Tape it to your monitor. Done.

```bash
# ===== CREATE =====
$ git worktree add <path> <branch>              # checkout existing branch
$ git worktree add -b <new-branch> <path>       # create branch + worktree
$ git worktree add --detach <path>              # detached HEAD worktree
$ git worktree add --no-checkout <path>         # create dir, defer checkout

# ===== INSPECT =====
$ git worktree list                             # all linked worktrees
$ git worktree list --porcelain                 # script-friendly

# ===== LIFECYCLE =====
$ git worktree remove <path>                    # delete (refuses if dirty)
$ git worktree remove --force <path>            # delete even if dirty
$ git worktree move <src> <dst>                 # relocate on disk
$ git worktree lock <path> --reason "..."       # protect from auto-prune
$ git worktree unlock <path>                    # release the lock
```

> `git worktree add ../<name> <branch>` — the one command that pays for the whole feature.

---

## Resources & Next Steps

**Resources**

- `git worktree --help` — the official manual. Everything in this post is in here.
- [git-scm.com/docs/git-worktree](https://git-scm.com/docs/git-worktree) — web version of the manual, with examples.
- [github.com/git/git/tree/Documentation](https://github.com/git/git/tree/Documentation) — upstream docs, including the locking rationale.
- `man git-worktree` — offline. Survives an internet outage.

**Next steps**

1. **Try it now** — `git worktree add ../playground main` in any repo.
2. **Wire aliases** — add `gwa` / `gwls` / `gwrm` to your shell config tonight.
3. **Pitch your team** — drop the cheat sheet above into your team's wiki.

> One repo. Many trees. Zero stash.
