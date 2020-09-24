# Write a Python program to concatenate all elements in a list into a string and return it.

x = int(input("ELEMENTS IN GROUP: "))
list = []
outstring = ""

for i in range(x):
	list.append(input(""))
	
def conjuagate(array, out):
	for i in array:
		out += str(i)
	return out
	
print(conjuagate(list, outstring))
