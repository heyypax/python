# While loops are used to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop is as follows:

#Example 1:

name = input("Enter your name: ")
while name == "":
    print("Please enter your name. We cannot proceed without it.")
    name = input("Enter your name: ")

print(f"Hello, {name}! Welcome!")

#Example 2:

age = int(input("Enter your age: "))
while age < 0:
    print("Age cannot be negative. Please enter a valid age to proceed.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old. You are eligible to order.")

#Example 3:

food = input("Enter your favorite food: ")
while not food == "q":
    print(f"You ordered {food}. That's great! We will add it to your order.")
    food = input("Please enter your favorite food. We cannot proceed without it. If you want to quit, enter 'q'.")
    print("Thank You!")
    
#Example 4:

number = int(input("Enter a number between 1 to 10: "))
while number < 1 or number > 10:
    print(f"Invalid {number}. Please enter a valid number between 1 to 10 to proceed.")
numner = int(input("Enter a number between 1 to 10 to proceed: "))
print(f"You entered {number}. Thank you for entering a valid number.")
