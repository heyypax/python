#Temperature conversion program.

unit = input("Enter your unit of temperature: (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * 9) / 5 + 32
    unit = "F"
    print(f"The temperature is {temp} {unit} Fahrenheit.")
elif unit == "F":
    temp = (temp - 32) * 5 / 9
    unit = "C"
    print(f"The temperature is {temp} {unit} Celsius.")
else:
    print("Invalid data entered. Please enter C for Celsius or F for Fahrenheit.")
    