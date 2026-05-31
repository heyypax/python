#Format specifiers in Python are used to format values into a string. They are placed inside the format() method or f-strings.
# {:flags} format a value based on what inserted in the flags.
# .(number)f - round to that many decimal places.(fixed point)
# :(number) - allocate that many spaces for the value.
# :3 - allocate and zero pad that many spaces for the value.
# :< - left justify the value within the allocated spaces.
# :> - right justify the value within the allocated spaces.
# :^ - center align the value within the allocated spaces.
# :+ - use a plus sign to indicate the value is positive.
# := - place the sign to the leftmost position of the number.
# :  - insert a space before positive numbers.
# :, - comma separator.

# Example usage:

price1 = -566.798677896
price2 = 5263.723889
price3 = 723897.23777

print(f"Price of item 1: {price1:+,.2f}")
print(f"Price of item 2: {price2:+,.2f}")
print(f"Price of item 3: {price3:+,.2f}")