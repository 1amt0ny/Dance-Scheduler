# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['scheduler_app_drag_n_drop.py'],
    pathex=[],
    binaries=[],
    datas=[('app_icon.png', '.'), ('scheduler.py', '.')],
    hiddenimports=['Foundation', 'tkinterdnd2'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Dance Scheduler',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app_icon.icns'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Dance Scheduler',
)
app = BUNDLE(
    coll,
    name='Dance Scheduler.app',
    icon='app_icon.icns',
    bundle_identifier='com.yourname.dancescheduler',
)
