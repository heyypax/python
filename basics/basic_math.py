#maths 
import math
x = 5
y = 3.5
z = 5

# The round() function rounds a number to a specified number of decimal places. If no decimal places are specified, it rounds to the nearest integer.

result = round(y)
print(result) # output: 4

# The abs() function returns the absolute value of a number, which is the distance of the number from zero on the number line. It always returns a non-negative value.

result = abs(x)
print(result) # output: 5

# The pow() function takes two arguments and returns the value of the first argument raised to the power of the second argument.

result = pow(z, 2)
print(result) # output: 25

# The max() function returns the largest of the input values, while the min() function returns the smallest of the input values.

result = max(x, y, z)
print(result) # output: 5

# The min() function returns the smallest of the input values.

result = min(x, y, z)
print(result) # output: 3.5

# The math module provides various mathematical functions and constants. To use the math module, you need to import it at the beginning of your Python program.

print(math.pi) # output: 3.141592653589793
print(math.e) # output: 2.718281828459045

# The math.sqrt() function returns the square root of a number, while the math.ceil() function rounds a number up to the nearest integer, and the math.floor() function rounds a number down to the nearest integer.

result = math.sqrt(x)
print(result) # output: 2.23606797749979

# The math.ceil() function rounds a number up to the nearest integer, and the math.floor() function rounds a number down to the nearest integer.

result = math.ceil(y)
print(result) # output: 4

# The math.floor() function rounds a number down to the nearest integer.

result = math.floor(y)
print(result) # output: 3


#Exercise 1: A program that calculates the circumfrence of the cicle.

radius = float(input("Enter the radius of the circle:"))
circumfrence = 2 * math.pi * radius

print(f"The circumfrence of the circle is {round(circumfrence, 2)} cm.") #result: The circumfrence of the circle is -- cm.


#Exercise 2: A program that calculates the area of a circle.

radius = float(input("Enter the radius of the circle:"))
area = math.pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)} cm square.") #result: The area of the circle is -- cm square.


#Exercise 3:

a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))

c = math.sqrt(pow(a, 2) + pow(b))
print(f"The length of the hypotenuse is {round(c, 2)} cm") #result: The length of the hypotenuse is -- cm.