#Typecasting is the process of converting a variable from one type to another. In Python, you can use built-in functions to perform typecasting. Here are some common typecasting functions:
# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string
# bool() - converts a value to a boolean

name = "Pax"
age = 25
height = 5.9
is_student = True

print(type(name)) # Output: <class 'str'>
print(type(age)) # Output: <class 'int'>
print(type(height)) # Output: <class 'float'>
print(type(is_student)) # Output: <class 'bool'>

age = float(age)
print(age)

age = str(age)
print(age)

name = bool(name)
print(name)