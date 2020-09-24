# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

'''

Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')

'''

nums = input("Input some sequnce of comma-seperated numbers: ")

list = nums.split(",")
tuple = tuple(list)

print("List : ", str(list) ,"\nTuple : ", str(tuple))