#nested loop - A loop within another loop is called a nested loop. (outer loop and inner loop)
#  outer loop
#     inner loop:
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol you want to see in the pattern: ")
for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
