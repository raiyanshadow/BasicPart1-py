# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20

x = int(input("INPUT FIRST INTEGER: "))
y = int(input("INPUT SECOND INTEGER: "))

def sum_check(int1, int2):
	z = int1 + int2
	
	if z >= 15 and z <= 20:
		return 20
	return z
	
print(sum_check(x, y))