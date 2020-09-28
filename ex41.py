# Write a Python program to check whether a file exists.

import os.path
from os import path

file = input("ENTER FILE NAME: ")
check = path.exists(file)

if check == True:
	print("Yes")
	exit()
print("No")