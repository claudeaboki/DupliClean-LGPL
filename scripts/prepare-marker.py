"""Insert a test-only, observable C source modification after upstream resets."""
import pathlib
import sys
p = pathlib.Path(sys.argv[1])
s = p.read_text(encoding='utf-8')
anchor = 'git checkout libavutil 1>>"${BASEDIR}"/build.log 2>&1\n'
assert s.count(anchor) == 1, 'Unexpected upstream build script'
# Upstream resets libavutil for each ABI. Apply after reset, preserving ABI.
patch = '''python3 - <<'DUPLICLEAN_SOURCE_MARKER' || return 1
from pathlib import Path
p = Path("libavutil/version.c")
s = p.read_text(encoding="utf-8")
old = "return FFMPEG_VERSION;"
assert s.count(old) == 1, "Unexpected FFmpeg source"
p.write_text(s.replace(old, 'return FFMPEG_VERSION "-DUPLICLEAN-LGPL-TEST";'), encoding="utf-8")
DUPLICLEAN_SOURCE_MARKER
'''
p.write_text(s.replace(anchor, anchor + patch), encoding='utf-8')
