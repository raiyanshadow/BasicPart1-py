# Write a Python program to print the following string in a specific format.

'''

Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are

'''

a = "Twinkle, twinkle, little star, "
b = "How I wonder what you are"
c = "Up above the world so high, "
d = "Like a diamond in the sky."

print(a + "\n\t" + b + "!\n\t\t" + c + "\n\t\t" + d + "\n" + a + "\n\t" + b)