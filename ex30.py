# Write a Python program that will accept the base and height of a triangle and compute the area.

h = float(input("ENTER HEIGHT: "))
w = float(input("ENTER WIDTH: "))

def triangle_area(width, height):
	return (width + height) / 2
	
print("AREA =", triangle_area(w, h))