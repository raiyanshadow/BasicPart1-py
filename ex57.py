# Write a program to get execution time for a Python method.

import time

def fibonacci(n):
	start = time.time()
	a = 0
	b = 1
	if n <= 0:
		print("Incorrect input")
	elif n == 1:
		return b
	else:
		for i in range(2,n):
			c = a + b
			a = b
			b = c
	end = time.time()
	return b, end-start
	
print("(End Result, time taken): \n", fibonacci(100000))