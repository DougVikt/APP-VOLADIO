import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["tkinter" , "pymsgbox" , "keyboard" ,"pycaw","pylnk3" ,"shutil" ,"inicializar"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="V-Audio",
    version="0.1",
    description="Ativa atalhos para alterar o volume do sistema.",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)