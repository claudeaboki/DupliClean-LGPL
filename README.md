# DupliClean LGPL — FFmpegKit 8.1.2 min rebuild laboratory

Independent build and replacement experiment for DupliClean 1.2.3 (20). No proprietary application source, user data, signing key or production bundle is required. **Not a certification of LGPL compliance.**

## Corresponding upstream revisions confirmed by the maintainer on 24 November 2026

- [FFmpegKit e15206ec7b29aff45853571f98308570166f2dca](https://github.com/maitrungduc1410/ffmpeg-kit/tree/e15206ec7b29aff45853571f98308570166f2dca) — [source ZIP](https://codeload.github.com/maitrungduc1410/ffmpeg-kit/zip/e15206ec7b29aff45853571f98308570166f2dca), collected SHA-256 `3ba03b8b512daa30181f8ef5cbc6a32fd15d2e8a2b89f67b38d4cd734cd9bfc3`.
- [FFmpeg 38b88335f99e76ed89ff3c93f877fdefce736c13](https://github.com/arthenica/FFmpeg/tree/38b88335f99e76ed89ff3c93f877fdefce736c13) — [source ZIP](https://codeload.github.com/arthenica/FFmpeg/zip/38b88335f99e76ed89ff3c93f877fdefce736c13), collected SHA-256 `c3453fbfc7ca25423f4984a83ceda01949d458a8bc04f9d68fab7c392f75b3ab`.
- [Upstream build workflow](https://github.com/maitrungduc1410/ffmpeg-kit/blob/e15206ec7b29aff45853571f98308570166f2dca/.github/workflows/android-build-scripts.yml), [Android script](https://github.com/maitrungduc1410/ffmpeg-kit/blob/e15206ec7b29aff45853571f98308570166f2dca/android.sh), [FFmpeg customizations](https://github.com/maitrungduc1410/ffmpeg-kit/blob/e15206ec7b29aff45853571f98308570166f2dca/scripts/android/ffmpeg.sh).
- [GNU LGPL v3](https://www.gnu.org/licenses/lgpl-3.0.html) and [FFmpeg legal information](https://ffmpeg.org/legal.html). Preserve upstream licenses and notices.

The local DUP071-42 audit matched all 18 native libraries to the supplier AAR and Gradle cache. Reference hashes in `scripts/reference-libraries.json` are for that audit. The workflow checks both ARM64 and ARMv7 NEON. The original recipe disables classic ARMv7, x86 and x86-64, but not ARMv7 NEON. It includes upstream build-time protocol/source changes. `scripts/prepare-marker.py` adds a **test-only** version suffix to `av_version_info()` after the upstream script resets libavutil; no ABI change intended. Never distribute this experimental AAR as the original vendor build.

## Run

1. In Actions, select **FFmpegKit 8.1.2 min - isolated rebuild**, Run workflow, `baseline`. Inspect the resulting artifact and logs.
2. If baseline succeeds, run `source-modified`. This rebuilds from source with a detectable marker, not an ELF metadata patch.
3. Download evidence and AAR; check `audit.json`. Bit-for-bit reproducibility is not assumed; differences must be investigated. Verify ABI compatibility and then test the modified library with an independently signed test APK on a controlled device. Do not overwrite the validated production AAB.

The workflow uses Ubuntu 22.04, JDK 17 and NDK r27c and the maintainer's min flags. It is intentionally manual and has no release, Maven publication, secrets, paid runner or application build. It does not guarantee available disk, dependency availability or success. It has not yet run on GitHub. Some generated config/log files may be removed by upstream cleanup; inspect evidence accordingly.

## Source availability and user rights

These commit-pinned downloads are source references. Before release, retain and make the verified corresponding source archives, applicable notices, build scripts and modifications durably available (e.g. public release assets, not expiring Actions artifacts). Audit any other applicable source dependencies. Document practical installation and relinking/replacement rights under LGPL v3. This repository alone does not demonstrate functional replacement or certify compliance.

Questions: see [DupliClean third-party notices](https://github.com/claudeaboki/dupliclean/blob/main/third-party-licenses.md).
