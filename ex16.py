# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.

num = int(input("Input integer : "))

if num > 17:
	dif = abs(2 * (num - 17))
else:
	dif = 17 - num

print("The result is", dif)