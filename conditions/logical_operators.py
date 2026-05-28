#Logical operators = evaluate and, or, not
#or = at least one statement must be true   
#and = both statements must be true
#not = inverts the result, will return false if the result is true

#or
temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled.")
else:
    print("The outdoor event is not cancelled.")


#and

temp = 20
is_sunny = True

if temp >= 20 and is_sunny:
    print("It is hot outside")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
elif 20 > temp > 0 and is_sunny:
    print("It is nice outside")


#not

temp = 20
is_sunny = False

if temp >= 20 and not is_sunny:
    print("It is hot outside")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
elif 20 > temp > 0 and not is_sunny:
    print("It is nice outside")