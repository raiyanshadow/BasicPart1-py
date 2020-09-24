# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

x = int(input("ENTER NUMBER 1: "))
y = int(input("ENTER NUMBER 2: "))
z = int(input("ENTER NUMBER 3: "))
sum = 0

if x == y or y == z or z == x:
	sum = 0
else:
	sum = x + y + z
	
print(str(sum))