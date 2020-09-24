# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

while True:
	try:
		fn = str(input("Input your first name: "))
		ln = str(input("Input your last name: "))
	except ValueError:
		print("Invalid Input(s)")
		continue
	else:
		break


print("\nYour name is " + ln + " " + fn)