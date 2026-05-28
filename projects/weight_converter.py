#Weight converter Program 

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K/P):")

if unit == "K":
    weight = weight * 2.20462
    unit = "lbs"
    print(f"Your weight is {weight} {unit}")
elif unit == "P":
    weight = weight / 2.20462
    unit = "kg"
    print(f"Your weight is {weight} {unit}")
else:
    print("Invalid data entered.")
    