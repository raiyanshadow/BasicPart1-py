''' 
Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
'''

principle = int(input("ENTER PRINCIPLE VALUE: "))
interest_rate = float(input("ENTER THE INTEREST RATE (1-100): "))
years = int(input("ENTER THE AMOUNT OF YEARS INVESTED: "))

future_value = principle * (1 + (interest_rate / 100)) ** years

print("Future Value: ", round(future_value, 2))
