# Write a Python program to locate Python site-packages.

import site

package_list = site.getsitepackages()
x = 0
print("\nYour site package paths are: \n")

for i in package_list:
	print("<><><><> " + str(package_list[x]))
	x += 1
print()