# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

x = int(input("1st number : "))
y = int(input("2nd number : "))
z = int(input("3rd number : "))

if x == y and y == z and x == z:
	sum = 3 * (x + y + z)
	print("The special sum is", sum)
else:
	sum = x + y + z
	print("The sum is", sum)

