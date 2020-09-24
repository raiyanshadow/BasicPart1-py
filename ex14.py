# Write a Python program to calculate number of days between two dates.

'''

Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

'''

from datetime import date

dateA = date(2014, 7, 2)
dateB = date(2014, 7, 11)

if dateB > dateA:
	datedif = dateB - dateA
else:
	datedif = dateA - dateB

print(datedif.days, "days")