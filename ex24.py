# Write a Python program to test whether a passed letter is a vowel or not.

lett = input("ENTER LETTER: ")
vowel_list = ["a", "e", "i", "o", "u"]

def vowel_check(char):
	if char in vowel_list:
		return "Vowel"
	return "Not a vowel"
	
print(vowel_check(lett))