# This is a sample Python program that prints "Hello World" to the console.
print("Helloo World")

#Variables = a vaiable is a container for storing data values. In Python, you don't need to declare the type of variable, it is dynamically typed. (strings, integers, float and boolean)

#strings = a string is a sequence of characters. It is used to store text data. Strings are enclosed in either single quotes (' ') or double quotes (" ").

first_name = "Pax"
food = "ramen"
place = "japan"
print(f"Hello {first_name}, do you you like {food}?")
print(f" You want to go {place} for vacations? ")

#integers = an integer is a whole number, positive or negative, without decimals. In Python, integers can be of any length, as long as they fit in memory.

age = 25
quantity = 5
print(f"You are {age} years old.")
print(f"You have {quantity} items in your cart.")

#Floats = a float is a number that has a decimal point. It is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts.

price = 15.55
size = 10.35
print(f"Price of rice is {price} rupees.")
print(f"Size of the pencil is {size} cm.")

#Booleans = a boolean is a data type that can have one of two values: True or False. It is used to represent the truth value of an expression.

is_student = True
is_employed = False
is_working = False
print(f"Is the boy standing there is a student? {is_student}")
print(f"Are you employed? {is_employed}")

if is_working:
    print("He is working.")
else:
    print("He is not working.")
