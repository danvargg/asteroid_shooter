"""Converts the game into an .exe file."""
import sys
import pygame
import cx_Freeze

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("src/start_game.py", base=base)]

cx_Freeze.setup(
    name="Asteroid Shooter",
    version="1.0",
    options={"build_exe": {"packages": ["pygame"], "include_files": ["src/graphics", "src/fonts", "src/sounds", "src/shooter"]}},
    executables=executables
)
