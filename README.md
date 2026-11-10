<!--
# SPDX-FileCopyrightText: Copyright 2026 Dozerr contributors
# SPDX-License-Identifier: GPL-3.0-or-later
-->

# Dozerr

Dozerr is a Nintendo Switch 2 emulator tuned for **Donkey Kong Bananza**. It is an independent
fork of [Lichii](https://github.com/zortos293/Lichii), which builds on Eglantine, Eden, yuzu and
Sudachi. It is not affiliated with Nintendo, with Lichii or with any of those projects.

Dozerr is in early development. Support is very limited, and only Donkey Kong Bananza is tuned.

## Where this comes from

- **Lichii** is the base and the upstream: Dozerr follows it and merges its updates.
- **Dozer**, an earlier fork of Anka, was tuned for the same game. Its performance work, above
  all the host-GPU read of Bananza's indirect terrain draws, is being brought across to this
  base one piece at a time. Dozer had an intermittent black shape with a white bloom halo on
  destroyed terrain that Lichii does not show, and moving to this base is meant to keep it away.

## Downloads and setup

Test builds are produced by this repository's GitHub Actions (the `dozer-test-builds` workflow,
Windows only) and are attached to each run as an artifact. There is no installer and no
automatic update yet.

On Windows, extract the whole archive and run **dozerr.exe** (the command-line program is
**dozerr-cli.exe**). Only use games and system files you have legally obtained. Games, keys and
firmware are not included.

### Existing saves and settings

Dozerr keeps Lichii's data directories and configuration keys, so an existing `user` folder
carries over. Back up your saves before testing a new build.

## Reporting problems

When [reporting an issue](https://github.com/Mvii7/Dozerr/issues), include the exact build (the
first line of the log names it), the game version, CPU, GPU and driver version, the settings and
steps that reproduce it, a screenshot, and the log of the affected session after checking it for
personal information. Do not upload game files, keys, firmware or private account information.

## Building

See the [build guide](docs/Build.md), the [user documentation](docs/user/README.md) and the
[coding guidelines](docs/Coding.md). Lichii's own readme is kept as
[docs/LICHII_README.md](docs/LICHII_README.md). Some inherited documentation and internal build
target names still use upstream names.

## Artwork

The Dozerr mark is a D whose flat edge is a bulldozer blade. It is drawn by
[dist/dozerr/dozerr_logo.py](dist/dozerr/dozerr_logo.py), which writes `dist/dozerr.ico`,
`dist/dozerr.icns`, `dist/dozerr.bmp` and `dist/dozerr.png`. Lichii's artwork, by YOB
(yobslab), is still in [dist/branding](dist/branding).

## Credits and license

Dozerr inherits the work of the Lichii, Eglantine, Eden, yuzu and Sudachi projects and their
contributors, including Eglantine's original developer Camille LaVey, and the work of Anka
(EddizEge) that Dozer was built on. Original copyright notices and third-party license files are
kept in the source tree.

See [LICENSE.txt](LICENSE.txt) and the source files for the applicable license terms.
