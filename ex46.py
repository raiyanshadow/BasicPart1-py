# Write a python program to get the path and name of the file that is currently executing.

import os

print("\n\n>>> Filename >>> " + __file__[2:])
print(">>> Path     >>> " + os.path.realpath(__file__) + "\n")