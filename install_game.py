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
    options={"build_exe": {"packages": ["pygame"], "include_files": ["src/graphics.png", "src/fonts.jpg"]}},
    executables=executables
)
