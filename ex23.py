# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

instring = input("ENTER STRING: ")
n = int(input("COPIES: "))
outstring = ""

for i in range(n):
	outstring += instring[:2]

print(outstring)