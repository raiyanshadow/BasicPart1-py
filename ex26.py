# Write a Python program to create a histogram from a given list of integers.

lett = input("ENTER CHARACTER: ")
x = int(input("ELEMENTS IN GROUP: "))
list = []
sout = ""
count = 0

for i in range(x):
	list.append(int(input()))

print("\nHistogram: \n")

for i in list:
	for j in range(list[count]):
		sout += lett
	
	print(sout)
	sout = ""
	count += 1