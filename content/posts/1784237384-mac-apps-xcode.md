+++ 
date = 2026-07-16T22:29:45+01:00
title = "Building and Shipping Mac and iOS Apps Without Ever Opening Xcode"
description = "A fully headless Xcode workflow using xcodebuild, notarytool, and XcodeGen — driven entirely from the command line and scriptable by AI coding agents."
slug = "mac-apps-without-xcode" 
tags = ["xcode", "macos", "ios", "cli", "developer-tools", "automation"]
categories = ["development"]
externalLink = ""
series = []
+++

- **Headless by design:** Xcode must be installed but never opened. All tools (`xcodebuild`, `notarytool`, `stapler`, `devicectl`) live inside `Xcode.app` and run from a shell. A one-time credential setup (Apple ID sign-in, Developer ID certificate, notarytool keychain profile) makes every subsequent build and deploy fully headless.
- **Project management:** `XcodeGen` replaces the `.xcodeproj` with a `project.yml` committed to git, regenerating the project on every build so the binary folder is never in version control.
- **One-command release:** `scripts/release.sh` runs the entire chain — archive, Developer ID sign, notarize, staple, verify, install to `/Applications`.
- **Two build paths:** `CODE_SIGNING_ALLOWED=NO` for fast unsigned builds (local/CI). `release.sh` for shipping with Developer ID signing and full notarization. Zero secrets in the repo — the private key stays in your login keychain, the notary credential in a keychain profile.
- **iOS too:** `xcodebuild archive` + `xcrun devicectl device install` deploys to a connected iPhone without the GUI.
- **Agent-native:** A `CLAUDE.md` tells your LLM coding tool the conventions — build paths, notary profile naming, scheme names. "Ship a build" becomes a single sentence.
- **One interactive step:** `notarytool store-credentials` requires typing an app-specific password once. Everything after that is scriptable end to end.

---

*This post is a condensed summary of [Scott Willsey's detailed guide](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/). All credit for the original workflow, the release script pattern, and the CLAUDE.md conventions goes to him.*

## Process Flow

{{< mermaid >}}
flowchart TD
    Setup["One-Time Credential Setup"]
    DevFast["Unsigned Build (Dev/CI)"]
    Release["Release Pipeline"]
    iOSPath["iOS Device Deploy"]

    Setup --> DevFast
    Setup --> Release
    Setup --> iOSPath

    DevFast --> Gen["xcodegen generate"]
    DevFast --> Test["swift test"]
    DevFast --> AdHoc["xcodebuild<br/>CODE_SIGNING_ALLOWED=NO"]

    Release --> Arch["1. Archive<br/>xcodebuild archive"]
    Arch --> Exp["2. Developer ID Export<br/>xcodebuild -exportArchive"]
    Exp --> Not["3. Notarize<br/>notarytool submit --wait"]
    Not --> Sta["4. Staple Ticket<br/>stapler staple"]
    Sta --> Ver["5. Verify<br/>spctl / stapler validate"]
    Ver --> Inst["6. Install to /Applications<br/>cp -R"]

    iOSPath --> iOSArch["xcodebuild archive<br/>-destination generic/platform=iOS"]
    iOSArch --> iOSInst["devicectl device install"]

    click Setup "#one-time-setup" "Go to One-Time Setup commands"
    click DevFast "#build--unsigned-quick-checks" "Go to unsigned build commands"
    click Gen "#build--unsigned-quick-checks" "Go to xcodegen generate"
    click AdHoc "#build--unsigned-quick-checks" "Go to unsigned build commands"
    click Release "#release-pipeline-mac" "Go to Release Pipeline commands"
    click Arch "#archive--export-manual-steps" "Go to archive/export commands"
    click Exp "#archive--export-manual-steps" "Go to archive/export commands"
    click Not "#notarization--stapling" "Go to notarization commands"
    click Sta "#notarization--stapling" "Go to notarization commands"
    click Ver "#verification" "Go to verification commands"
    click Inst "#release-pipeline-mac" "Go to Release Pipeline commands"
    click iOSPath "#ios-device-deployment" "Go to iOS deployment commands"
    click iOSArch "#ios-device-deployment" "Go to iOS deployment commands"
    click iOSInst "#ios-device-deployment" "Go to iOS deployment commands"

    style Setup fill:#1e293b,color:#fff,stroke:#475569
    style DevFast fill:#1e3a5f,color:#fff,stroke:#2563eb
    style Release fill:#3b1f3b,color:#fff,stroke:#7e22ce
    style iOSPath fill:#1a3a2a,color:#fff,stroke:#059669
{{< /mermaid >}}

Click any node in the diagram to jump to its corresponding command table.

## Command Reference

### One-Time Setup

| Command | Purpose |
|---|---|
| `xcode-select -p` | Check which toolchain is active |
| `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer` | Switch to Xcode's full toolchain |
| `brew install xcodegen` | Install XcodeGen for project generation |
| `sudo xcodebuild -license accept` | Accept Xcode license agreement |
| `sudo xcodebuild -runFirstLaunch` | Install Xcode additional components |
| `xcrun notarytool store-credentials <App-Name> --apple-id "<email>" --team-id <TEAM-ID>` | Store notarization credential (prompts for app-specific password) |
| `xcrun notarytool history --keychain-profile <App-Name>` | Verify notarization credential is stored |
| `cp Local.xcconfig.example Local.xcconfig` | Create local config file for team ID and bundle prefix |

### Build — Unsigned (Quick Checks)

| Command | Purpose |
|---|---|
| `swift test` | Run unit tests (SPM, no Xcode build) |
| `xcodegen generate` | Regenerate `.xcodeproj` from `project.yml` |
| `xcodebuild -project <App>.xcodeproj -scheme <App>-macOS -destination 'platform=macOS' CODE_SIGNING_ALLOWED=NO build` | Compile macOS app (ad-hoc, unsigned) |
| `xcodebuild -project <App>.xcodeproj -scheme <App>-iOS -destination 'generic/platform=iOS Simulator' CODE_SIGNING_ALLOWED=NO build` | Compile iOS app for Simulator (unsigned) |

### Release Pipeline (Mac)

| Command | Purpose |
|---|---|
| `./scripts/release.sh` | Full chain: archive → Developer ID sign → notarize → staple → install to `/Applications` |
| `<APP>_NOTARY_PROFILE=<name> ./scripts/release.sh` | Override the notary profile for a different identity |

### Archive & Export (Manual Steps)

| Command | Purpose |
|---|---|
| `xcodebuild -project <App>.xcodeproj -scheme <App>-macOS -configuration Release -derivedDataPath build/derived -archivePath build/<App>.xcarchive -allowProvisioningUpdates archive` | Archive the macOS app |
| `xcodebuild -exportArchive -archivePath build/<App>.xcarchive -exportPath build/Export -exportOptionsPlist build/ExportOptions.plist -allowProvisioningUpdates` | Export Developer ID-signed `.app` from archive |

### Notarization & Stapling

| Command | Purpose |
|---|---|
| `ditto -c -k --keepParent <App>.app notarize.zip` | Package app into zip for upload |
| `xcrun notarytool submit notarize.zip --keychain-profile <App-Name> --wait` | Submit for notarization (blocks until complete) |
| `xcrun stapler staple <App>.app` | Attach notarization ticket to the app bundle |
| `xcrun stapler validate <App>.app` | Verify ticket is attached |

### Verification

| Command | Purpose |
|---|---|
| `codesign -dv --verbose=4 /Applications/<App>.app` | Show signing identity and certificate chain |
| `spctl -a -vvv -t exec /Applications/<App>.app` | Check Gatekeeper acceptance |
| `xcrun stapler validate /Applications/<App>.app` | Validate notarization ticket on installed app |

### iOS Device Deployment

| Command | Purpose |
|---|---|
| `xcodebuild -project <App>.xcodeproj -scheme <App>-iOS -destination 'generic/platform=iOS' -allowProvisioningUpdates -derivedDataPath build/ios archive -archivePath build/<App>-iOS.xcarchive` | Archive iOS app for device deployment |
| `xcrun devicectl list devices` | List connected devices and their UDIDs |
| `xcrun devicectl device install app --device <UDID> path/to/<App>.app` | Install `.app` onto a connected iPhone |
