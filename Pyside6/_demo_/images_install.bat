nuitka ^
  --standalone ^
  --enable-plugin=pyside6 ^
  --assume-yes-for-downloads ^
  --windows-console-mode=disable ^
  --output-dir=bin ^
  --remove-output ^
  --nofollow-import-to=tkinter,turtle,test,unittest ^
  --windows-icon-from-ico=C:\\IDE\\PyCharm\\bin\\pycharm.ico ^
  --lto=yes ^
  --jobs=8 ^
  --output-filename=DisplayTime ^
  --include-data-dir=images=images ^
  image_demo.py