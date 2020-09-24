# Write a Python program to check whether a specified value is contained in a group of values.

n = int(input("ENTER INTEGER: "))
x = int(input("ELEMENTS IN GROUP: "))
list = []

for i in range(x):
	list.append(input(""))
	
def num_check(int):
	if int in list:
		return True
	return False

print(num_check(int))