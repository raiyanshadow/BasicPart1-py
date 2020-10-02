# Write a python program to find the sum of the first n positive integers.

n = int(input("ENTER A NATURAL NUMBER: "))

def n_sum(f):
	list = []
	sum = 0
	for i in range(1, f + 1):
		list.append(i)
	
	for m in list:
		sum += m
	return sum

print(n_sum(n))