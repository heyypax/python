# name = input("Type your name: ")
# one_number = input("Enter youur phone number #: ")
# result = len(name)
# result = name.find("a") # find the index of the first occurrence of "a" in the name.
# result = name.rfind("b") # find the index of the last occurrence of "b" in the name.
# result = name.capitalize() # capitalize the first letter of the name.
# name = name.upper() # convert the name to uppercase.
# name = name.lower() # convert the name to lowercase.
# name = name.isdigit() # check if the name consists of only digits.
# name = name.isalpha() # check if the name consists of only alphabetic characters.

# result = phone_number.count("-") # count the number of occurrences of "-" in the phone number.
# phone_number = phone_number.replace("-", " ") # replace all occurrences of "-" with a space in the phone number.
# print(phone_number)

# print(help(str)) # prints the documentation for the str class.



# validate user input exercise.
# 1. username is more than 12 characters.
# 2. username must not contain spaces.
# 3. username must not contain special characters.

#Exercise: 

username = input("Enter your username: ")

if len(username) > 10:
    print("Username must be less than 10 characters.")
elif not username.find(" ") == -1:
    print("Username must not contain spaces. Please try again without spaces. ")
elif not username.isalpha():
    print("Username must not contain special characters. Please try again without special characters. ")
else:
    print(f"Username is valid. Welcome, {username}!")