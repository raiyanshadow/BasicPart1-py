# Write a Python program to calculate the hypotenuse of a right angled triangle.

import math

print("\n |\ ")
print(" | \ ")
print("A|  \C ")
print(" |   \ ")
print(" |____\ ")
print("    B ")

print("\n Using the above diagram awnser the following questions:")

A = int(input("A measurement: "))
B = int(input("B measurement: "))
unit = input("Unit of measurement? ")

C = math.sqrt((A**2 + B**2))
print("C =", C, unit)