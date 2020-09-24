# Write a Python program to print the calendar of a given month and year.

import calendar

month = int(input("Input month : "))
year = int(input("Input year : "))

print(calendar.month(year, month))