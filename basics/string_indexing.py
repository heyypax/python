#String indexing: accessing elements of asequence using [] and index operators.
# [start : end : step] - slicing syntax for strings.
# start - the index of the first character to include in the slice (default is 0).
# end - the index of the first character to exclude from the slice (default is the length of the string).
# step - the number of characters to skip between each character in the slice (default is 1).

card_number = "1782-8172-6723-5632"

# print(card_number[0]) ; # prints the first character of the card number, which is "1".
# print(card_number[5]) ; # prints the sixth character of the card number, which is "-".
# print(card_number[-1]) ; # prints the last character of the card number
# print(card_number[-4]) ; # prints the fourth character from the end of the card number, which is "6".
# print(card_number[0:4]) ; # prints the first four characters of the card number, which is "1782".
# print(int(card_number[5:9])) ; # prints the characters from index 5 to index 8 of the card number, which is "8172".
# print(card_number[0:19:5]) ; # prints every 5th character of the card number, starting from index 0, which is "1865".
# print(int(card_number[::5])) ; # prints every 5th character of the card number, starting from index 0, which is "1865".

# last_digits = card_number[-4:] ; # prints the last four characters of the card number, which is "5632".
# print(f"XXXX-XXXX-XXXX-{last_digits}") ; # prints "XXXX-XXXX-XXXX-5632", masking the first 12 characters of the card number.

# card_number = card_number[: :-1] ; # reverses the card number by slicing it with a step of -1.
# print(int(card_number)) ; # prints the reversed card number, which is "2365-3276-2718-2871".


