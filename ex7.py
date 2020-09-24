# Write a Python program to accept a filename from the user and print the extension of that.

'''

Sample filename : abc.java
Output : java

'''

flnm = input("Input a filename : ")

list = flnm.split(".")

print("File type is : ", str(list[1]))