# -*- mode: python -*-

block_cipher = None


a = Analysis(['主界面.py'],
             pathex=['btnLabel.py', 'Draw', 'fuyin', 'Help', 'houbiyin', 'interface', 'ise', 'kaiweiyun', 'other', 'qianbiyin', 'Recorder', 'test_Dialog', 'yuanyin', 'yuanyinshewei', 'C:\\Users\\linpe\\作业\\数据结构与算法\\大作业\\数算大作业'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='主界面',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='主界面')
