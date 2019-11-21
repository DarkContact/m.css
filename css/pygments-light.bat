echo F|xcopy /Y pygments-light.py C:\Development\Python\Python38-32\Lib\site-packages\pygments\styles\light.py
pygmentize -f html -S light -a .m-code > pygments-light.css