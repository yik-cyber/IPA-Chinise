# -*- mode: python -*-

block_cipher = None


a = Analysis(['������.py'],
             pathex=['btnLabel.py', 'Draw', 'fuyin', 'Help', 'houbiyin', 'interface', 'ise', 'kaiweiyun', 'other', 'qianbiyin', 'Recorder', 'test_Dialog', 'yuanyin', 'yuanyinshewei', 'C:\\Users\\linpe\\��ҵ\\���ݽṹ���㷨\\����ҵ\\�������ҵ'],
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
          name='������',
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
               name='������')
