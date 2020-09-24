# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

str = input("INPUT STRING: ")
n = int(input("# OF COPIES: "))


def str_copy(txt, num):
	output = ""
	for i in range(num):
		output = output + txt
	return output
	
print(str_copy(str, n))