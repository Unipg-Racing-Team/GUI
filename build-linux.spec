# -*- mode: python ; coding: utf-8 -*-
import json

def load_configs():
    json_data = ''
    with open('package.json', 'r') as f:
       json_data = json.loads(f.read())

    return json_data

block_cipher = None

added_files = [
    ('./gui', 'gui'),
]

configs = load_configs()

a = Analysis(
    ['./src/index.py'],
    pathex=['./dist'],
    binaries=[],
    datas=added_files,
    hiddenimports=['clr'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=configs['name'],
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
