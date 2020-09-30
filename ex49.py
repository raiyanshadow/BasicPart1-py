# Write a Python program to list all files in a directory in Python.

from pathlib import Path
import os

print("\nAll child nodes in directory: ")

p = Path(os.path.dirname(__file__))

for child in p.iterdir(): print(child)