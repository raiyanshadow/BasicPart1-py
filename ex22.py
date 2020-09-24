# Write a Python program to count the number 4 in a given list.

n = input("ENTER COMMA SEPERATED NUMBERS: ")
n_list = n.split(",")
count = 0

for i in n_list:
	if '4' in n_list:
		n_list.remove('4')
		count += 1

print("You have entered the number 4,", count, "times.")