# Write a Python program which accepts the radius of a circle from the user and compute the area.

'''

Sample Output :
r = 1.1
Area = 3.8013271108436504

'''


import math

pi = math.pi

while True:
	try:
		radi = float(input("Radius? "))
	except ValueError or math.nan:
		print("Not a number! Try Again!")
		continue
	else:
		break


print("Area = " + str(math.pow(radi, 2) * pi))