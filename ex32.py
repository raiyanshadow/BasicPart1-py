# Write a Python program to get the least common multiple (LCM) of two positive integers.

x = int(input("ENTER A NATURAL NUMBER, X: "))
y = int(input("ENTER A NATURAL NUMBER, Y: "))

def factor_list(int1, int2):
	overlord = max(int1, int2)
	list = []
	for i in range(overlord):
		if i > 1:
			if int1 % i == 0 and int2 % i == 0:
				list.append(i)
	return list
	
def gcd(array):
	gcd_max = 0
	for i in array:
		if i > gcd_max:
			gcd_max = i
	return gcd_max

def lcm(int1, int2, gcd_int):
	return (int1 * int2) / gcd_int
	
gcd_xy = gcd(factor_list(x, y))	
lcm_xy = lcm(x, y, gcd_xy)

print("LCM of", x,"and", y, "is", lcm_xy)
