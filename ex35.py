# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

x = int(input("INPUT FIRST INTEGER: "))
y = int(input("INPUT SECOND INTEGER: "))

def true_check(int1, int2):
	if int1 == int2:
		return True
	elif int1 + int2 == 5:
		return True
	elif int1 - int2 == 5 or int2 - int1 == 5:
		return True
	return False

print(true_check(x, y))