# Write a Python program to determine profiling of Python programs. 
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.
# Note: Since there is a bubble sort function and 100000 number counter, results may take up to a minute to show up
# Note: 10 second pause has been added between each function execution so you may look at the results, timer edit is welcom

import cProfile
import random
import time

randlist = []

for x in range(0, 10000):
		randlist.append(random.randint(0, 1000000))
print(randlist)
# put your own functions here

# bubble sort function stolen from runestone.academy, cause im lazy :) 
def function_a(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1
	   
cProfile.run('function_a(randlist)')
time.sleep(10)                   # edit this for your preference
	
def function_b():
	for i in range(0, 100000):
		print(i)
	return True
	
cProfile.run('function_b()')