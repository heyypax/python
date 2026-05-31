#Python compound interest calculator program.

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than 0. Please enter a valid amount to proceed.")

while rate <= 0:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please enter a valid rate to proceed.")

while time <= 0:
    time = float(input("Enter the time period in years: "))
    if time <= 0:
        print("Time period must be greater than 0. Please enter a valid time period to proceed.")

amount = principle * pow(1 + rate / 100, time)
print(f"The total amount after {time} years will be ${amount:.2f}")