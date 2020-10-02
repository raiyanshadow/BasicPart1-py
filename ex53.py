# Write a python program to access environment variables.

import os

print("All your enviromental variables:\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n\n\n", os.environ)
print("\n\n\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n\n\n")
n = input("ENTER A SPECIFIC VARIABLE: ")
	
print("\n\nVariable " + n + ":", os.environ[n])
