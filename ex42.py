# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import sys

def bit_check() -> bool:
	return sys.maxsize > 2**32
	
if bit_check() == True:
	print("64-Bit")
	exit()
print("32-Bit")