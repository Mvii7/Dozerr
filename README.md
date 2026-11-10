<!--
# SPDX-FileCopyrightText: Copyright 2026 Dozerr contributors
# SPDX-License-Identifier: GPL-3.0-or-later
-->

<p align="center">
  <img src="dist/dozerr/dozerr_banner_v2.png" alt="Dozerr" width="600">
</p>

# Dozerr

Dozerr is a Nintendo Switch 2 emulator tuned for **Donkey Kong Bananza**. It is an independent
fork of [Lichii](https://github.com/zortos293/Lichii), which builds on Eglantine, Eden, yuzu and
Sudachi. It is not affiliated with Nintendo, with Lichii or with any of those projects.

Dozerr is in early development. Support is very limited.

## Downloads and setup

Test builds are produced by this repository's GitHub Actions (the `dozerr-test-builds` workflow,
Windows only) and are attached to each run as an artifact. Releases, once there are any, go on this
repository's [releases page](https://github.com/Mvii7/Dozerr/releases); Dozerr's built-in updater
(kept from Lichii) checks that page, not Lichii's.

On Windows, extract the whole archive and run **dozerr.exe** (the command-line program is
**dozerr-cli.exe**). Only use games and system files you have legally obtained. Games, keys and
firmware are not included.

### Saves and settings

Dozerr uses the same data directories as Lichii and Eden. Back up your saves before testing a
new build, or give each test build its own fresh portable `user` folder.

## Reporting problems

When [reporting an issue](https://github.com/Mvii7/Dozerr/issues), include the exact build (the
first line of the log names it), the game version, CPU, GPU and driver version, the settings and
steps that reproduce it, a screenshot, and the log of the affected session after checking it for
personal information. Do not upload game files, keys, firmware or private account information.

## Building

See the [build guide](docs/Build.md), the [user documentation](docs/user/README.md) and the
[coding guidelines](docs/Coding.md). Some inherited documentation and internal build target names
still use upstream names.

## Artwork

The Dozerr mark is a D whose flat edge is a bulldozer blade. It is drawn by
[dist/dozerr/dozerr_logo.py](dist/dozerr/dozerr_logo.py), which writes `dist/dozerr.ico`,
`dist/dozerr.icns`, `dist/dozerr.bmp`, `dist/dozerr.png` and the banner above.

## Credits and license

Dozerr inherits the work of the Lichii, Eglantine, Eden, yuzu and Sudachi projects and their
contributors, including Eglantine's original developer Camille LaVey, and the work of Anka
(EddizEge). Original copyright notices and third-party license files are
kept in the source tree.

See [LICENSE.txt](LICENSE.txt) and the source files for the applicable license terms.
