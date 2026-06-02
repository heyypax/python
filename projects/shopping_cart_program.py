#Shopping Cart Pogram

foods = []
prices = []
total = 0

while True:
    food = input("Enter the name of food item you want to add that in your cart. (or type 'done' to finish): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("------Your Shopping Cart-----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nTotal price of your cart is ${total:.2f}")