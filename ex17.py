# Write a Python program to test whether a number is within 100 of 1000 or 2000.

def checkNear(n):
	return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)) 

print(checkNear(800))
print(checkNear(1100))
print(checkNear(1500))
print(checkNear(2156))
print(checkNear(2001))
print(checkNear(5300))
print(checkNear(2097))