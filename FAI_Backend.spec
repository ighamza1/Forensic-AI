# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules


# =========================================================
# Hidden imports
# =========================================================

hiddenimports = []

hiddenimports += collect_submodules("torch")
hiddenimports += collect_submodules("torchvision")
hiddenimports += collect_submodules("flask")
hiddenimports += collect_submodules("werkzeug")
hiddenimports += collect_submodules("reportlab")


# =========================================================
# Application files
# =========================================================

datas = [

    # Flask templates
    ("templates", "templates"),

    # CSS / JavaScript / Images / Uploads
    ("static", "static"),

    # PyTorch models
    ("models", "models"),

    # Utility Python modules
    ("utils", "utils"),

]


# =========================================================
# Analysis
# =========================================================

a = Analysis(

    ["run_fai.py"],

    pathex=[
        "."
    ],

    binaries=[],

    datas=datas,

    hiddenimports=hiddenimports,

    hookspath=[],

    hooksconfig={},

    runtime_hooks=[],

    excludes=[],

    noarchive=False,

    optimize=0,

)


# =========================================================
# Python archive
# =========================================================

pyz = PYZ(
    a.pure
)


# =========================================================
# Executable
# =========================================================

exe = EXE(

    pyz,

    a.scripts,

    [],

    exclude_binaries=True,

    name="FAI_Backend",

    debug=False,

    bootloader_ignore_signals=False,

    strip=False,

    upx=False,

    console=True,

    disable_windowed_traceback=False,

    argv_emulation=False,

    target_arch=None,

    codesign_identity=None,

    entitlements_file=None,

)


# =========================================================
# Collect everything
# =========================================================

coll = COLLECT(

    exe,

    a.binaries,

    a.datas,

    strip=False,

    upx=False,

    upx_exclude=[],

    name="FAI_Backend",

)