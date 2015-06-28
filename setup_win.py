import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
  base = "Win32GUI"

setup(name = "MyPoker Beta",
version = "0.4",
description = "converter",
executables = [Executable("MyPoker.py", base=base)])