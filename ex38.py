''' 
Write a Python program to solve (x + y) * (x + y). 

Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2) = 49

'''

x = int(input("ENTER INTEGER: "))
y = int(input("ENTER ANOTHER INTEGER: "))
result = (x + y)**2


print("({0} + {1})^2 = {2}".format(x, y, result))