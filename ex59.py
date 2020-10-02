# Write a Python program to convert height (in feet and inches) to centimeters.

f = int(input("FEET: "))
i = int(input("INCHES: "))

cm = (f*30.48)+(i*2.54)

print("Feets and inches to cm: ", cm,"cm")