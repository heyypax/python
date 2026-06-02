#Collection - single variable that can hold multiple values.
# List - ordered, changeable, allows duplicate values. Lists are defined using square brackets []. 

fruits = ["apple", "banana", "cherry", "apple", "kiwi"]
for fruit in fruits:
    print(fruit)

print(dir(fruits)) #dir() function returns a list of the attributes and methods of any object (string, int, list, etc).
print(len(fruits)) #len() function returns the number of items in an object. In this case, it will return the number of items in the list 'fruits'.
print(type(fruits)) #type() function returns the type of the specified object. In this case, it will return <class 'list'>, indicating that 'fruits' is a list
print(fruits[0]) #Accessing the first item in the list using index 0. This will print "apple".
print(fruits[1]) #Accessing the second item in the list using index 1. This will print "banana".
print(fruits[2]) #Accessing the third item in the list using index 2. This will print "cherry".
print(help(fruits)) #help() function is used to display the documentation of a module, class, function, or method. In this case, it will show the documentation for the list object, including its methods and attributes.
print("apple" in fruits) #This will check if the string "apple" is present in the list 'fruits'. It will return True because "apple" is indeed in the list.

