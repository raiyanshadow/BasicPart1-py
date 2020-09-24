# Write a Python program to add two objects if both objects are an integer type.

MEASURE = 0

x = 65
y = "foo"

z = 3
m = "bar"

a = [3, 4, 1, 0]
b = {(6, 7), (1, 1), (2, 6)}

r = 'A'
i = "hello, world"

t = 45.32
e = 6431.45

u = 67
s = 8889

def int_check(o1, o2):
	global MEASURE
	if not (isinstance(o1, int) and isinstance(o2, int)):
		MEASURE += 1
		if MEASURE == 10:
			return """ MAXIMUM CORE PUNCTUTIONS:
						usage: python .\ex36.py ...
						
						*-> (extern __main__, class_alpha)
						*-> int_check(o1, o2):
						*-> print(recursive(__ main *& object*alpha __, __ main *& object*beta __))
						
						PROTOCOL MEASURES THREATENED:
							
							CORE CONTAMINATION SIGMA ACTIVATE:
							
							-----------------------------------
							-----------------------------------
							===================================
							===================================
							-----------------------------------
							-----------------------------------
							
							CORE CONTAMINATION SIGMA NEUTRALIZED $$
						
						%% END SYSTEM REHABILIATATION 
						%% END THREAT ANALYSIS POINTER
			"""
		
		elif MEASURE == 11:
			quit()
			
		return """ FATAL ERROR OVERLOADED:
					usage: python .\ex36.py ...
					
					*-> (extern __main__, class_alpha)
					*-> int_check(o1, o2):
					*-> print(recursive(__ main *& object*alpha __, __ main *& object*beta __))
				
					PROTOCOL MEASURSES BYPASSED:
						ERROR CODE 11-34XZ-QT7:
							BYPASS MEASURES 1 times
					
					%% POWER GENERATION CATARCONIATION END %%
		"""
	
	return o1 + o2
	
print(int_check(x, y))
print(int_check(z, m))
print(int_check(a, b))
print(int_check(r, i))
print(int_check(t, e))
print(int_check(u, s))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
print(int_check(t, e))
