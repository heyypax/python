#For_loop - you can execute a bloack of code a fixed number of times. You can iterate over a sequence (like a list, tuple, string) or other iterable objects. The syntax for a for loop is as follows:

for x in range(1, 11):
    print(x)

print("Happy New Year!") 

#continue statement - is used to skip the current iteration of a loop and move to the next iteration. It is often used when you want to skip certain conditions or values in a loop. The syntax for the continue statement is as follows:
#reverse(range(1, 11)) - will reverse the order of the numbers from 1 to 10.
#break statement - is used to exit a loop prematurely when a certain condition is met. It is often used when you want to stop the loop based on a specific condition. The syntax for the break statement is as follows:

#Example 1:
for x in range(1, 21):
    if x == 13:
        continue
    print(x)

#Example 2:
for x in reversed(range(1, 11)):
    print(x)

#Example 3:
for x in range(1, 21):
    if x == 13:
        break
    print(x)