#if do some code only if a certain condition is true else something else


#Example 1:

age = int(input("Enter your age: "))
if age >= 45:
    print("You are too old to vote.")
elif age >= 18:
    print("You are eligible to vote.")
elif age < 0:
    print("Invalid age is provided.")
else:
    print("You are not eligible to vote.")


    #Example 2: 

    name = input("Type your name:")
    if name == " ":
        print("You did not typed anything.")
    else:
        print(f"Hello {name}!")


        #Example 3:
        is_online = True
        
        if is_online:
            print("You are online")
        else:
            print("You are offline.")

