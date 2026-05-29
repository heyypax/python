#Conditional expressions are a way to assign a value to a variable based on a condition. They are also known as ternary operators because they take three operands: a condition, a value if the condition is true, and a value if the condition is false.
# print or assign one of two values based on a condition
# X if condition else Y

num = 7

#print("Positive" if num > 0 else "Negative")

logged_in = False

age = 18
temp = 40

print("Welcome!" if logged_in else "Please log in to continue.")

print("you are an adult" if age>=20 else "You need to wait until you are 20 to be an adult")
print("It is hot outside" if temp > 35 else "The weather is nice outside")
