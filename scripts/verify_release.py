#!/usr/bin/env python3
"""Check original downloads and APK assets without requiring signing secrets."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


def main():
    metadata = json.loads((ROOT / 'apk-validation.json').read_text())
    version = json.loads((ROOT / 'package.json').read_text())['version']
    if version != metadata['version']:
        raise ValueError('Package and APK metadata versions differ')
    manifest = ET.parse(ROOT / 'app/src/main/AndroidManifest.xml').getroot()
    android = '{http://schemas.android.com/apk/res/android}'
    if (manifest.get('package') != metadata['package']
            or manifest.get(android + 'versionName') != version
            or manifest.get(android + 'versionCode') != str(metadata['versionCode'])):
        raise ValueError('Source manifest and release metadata differ')
    if manifest.findall('uses-permission'):
        raise ValueError('Review Android permissions before publishing')

    prefix = f'Emlekor-{version}'
    expected_names = {prefix + '.apk', prefix + '-forraskod.zip'}
    lines = (ROOT / 'SHA256SUMS').read_text().splitlines()
    checksums = {}
    for line in lines:
        digest, name = line.split('  ', 1)
        if name not in expected_names or name in checksums:
            raise ValueError('Unexpected or duplicate checksum entry')
        checksums[name] = digest
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise ValueError(f'Checksum mismatch: {name}')
    if set(checksums) != expected_names:
        raise ValueError('Missing release checksum')
    if checksums[prefix + '.apk'] != metadata['sha256']:
        raise ValueError('APK hash differs from original validation metadata')

    with ZipFile(ROOT / (prefix + '.apk')) as apk:
        if apk.testzip() is not None:
            raise ValueError('Corrupt APK archive')
        assets = sorted((ROOT / 'app/src/main/assets').rglob('*'))
        assets = [p for p in assets if p.is_file()]
        names = {'assets/' + p.relative_to(ROOT / 'app/src/main/assets').as_posix()
                 for p in assets}
        if names != {name for name in apk.namelist() if name.startswith('assets/') and not name.endswith('/')}:
            raise ValueError('APK and source asset lists differ')
        for source in assets:
            name = 'assets/' + source.relative_to(ROOT / 'app/src/main/assets').as_posix()
            if apk.read(name) != source.read_bytes():
                raise ValueError(f'APK asset differs: {name}')
    with ZipFile(ROOT / (prefix + '-forraskod.zip')) as archive:
        if archive.testzip() is not None:
            raise ValueError('Corrupt original source archive')
    print(f'OK: {version}; both SHA-256 hashes, ZIP integrity and {len(assets)} APK assets verified.')
    print('This check does not revalidate Android signing or perform a device test.')


if __name__ == '__main__':
    main()
