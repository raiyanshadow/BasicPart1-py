# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math

print("Enter like this: x,y\n")

pair1 = input("ENTER 1ST ORDERED PAIR: ")
pair2 = input("ENTER 2ND ORDERED PAIR: ")

pair1_list = pair1.split(",")
pair2_list = pair2.split(",")

distance_formula = math.sqrt((int(pair2_list[0]) - int(pair1_list[0])) ** 2 + (int(pair2_list[1]) - int(pair1_list[1])) ** 2)

print("Distance between ordered pairs:", distance_formula)