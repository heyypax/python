fruits =     ["apple", "banana", "cherry", "apple", "kiwi"]
vegetables = ["carrot", "broccoli", "spinach", "carrot", "pepper"]
meats =      ["chicken", "beef", "pork", "chicken", "fish"]
# A 2D collection is a collection of collections. In this case, we can create a list of lists to represent a 2D collection of fruits, vegetables, and meats.

food = [fruits, vegetables, meats]
print(food) #This will print the entire 2D collection, which is a list of lists. The output will show the three lists (fruits, vegetables, and meats) as elements of the main list 'food'.
print(food[0]) #This will access the first element of the 2D collection, which is the 'fruits' list. It will print ["apple", "banana", "cherry", "apple", "kiwi"].

num_pad = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9],
    ["*", 0, "#"]
]

for row in num_pad:
    for num in row:
        print(num, end=" ") #This will print each number in the 2D collection 'num_pad' in a formatted way, with each number separated by a space. The 'end=" "' argument in the print function ensures that the output is printed on the same line with a space between each number.
    print() #This will print a newline after each row of numbers, ensuring that the next row starts on a new line.