"""Compare reconstructed libraries to the known release; no signing or publishing."""
import hashlib, json, pathlib, shutil, sys, zipfile
root, out, variant = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]), sys.argv[3]
reference = json.loads((pathlib.Path(__file__).parent / 'reference-libraries.json').read_text())
files = list(root.rglob('*.aar'))
if len(files) != 1:
    raise RuntimeError(f'Expected one AAR, found: {files}')
p = files[0]
sha = lambda b: hashlib.sha256(b).hexdigest()
results = []
marker = b'DUPLICLEAN-LGPL-TEST'
with zipfile.ZipFile(p) as z:
    if z.testzip() is not None: raise RuntimeError('Corrupt AAR')
    names = {n[4:] for n in z.namelist() if n.startswith('jni/') and n.endswith('.so')}
    if names != set(reference): raise RuntimeError(f'Unexpected JNI inventory: {sorted(names ^ set(reference))}')
    for n in sorted(names):
        b = z.read('jni/' + n)
        if not b.startswith(b'\x7fELF'): raise RuntimeError(f'Not ELF: {n}')
        results.append(dict(library=n,sha256=sha(b),vendor_sha256=reference[n],same_as_vendor=sha(b)==reference[n],marker_present=marker in b))
    util = [r for r in results if '/libavutil' in r['library']]
    if len(util)!=2 or any(r['marker_present'] != (variant=='source-modified') for r in util):
        raise RuntimeError('Unexpected libavutil marker state')
shutil.copy2(p,out / ('ffmpeg-kit-min-'+variant+'.aar'))
(out/'audit.json').write_text(json.dumps(dict(variant=variant,aar_sha256=sha(p.read_bytes()),libraries=results,count=len(results),identical_vendor_count=sum(r['same_as_vendor'] for r in results),runtime_replacement_tested=False),indent=2)+'\n')
print('AAR rebuilt; inventory and marker checked. Runtime replacement NOT tested.')
