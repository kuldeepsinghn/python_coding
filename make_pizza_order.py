print("Welcome to the pizza world :) ")
size = input("Enter the size of pizza which one you want!")
add_pepperoni = input("Do you want add pepperoni in your pizza sir!")
add_extra_cheese = input("do you want some extra cheese in your pizza sir!")
bill = 0

if size == "S":
    bill += 10
elif size == "M":
    bill += 15
else:
    bill += 20

if add_pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

if add_extra_cheese == "y":
    bill += 1

print(f"you have to pay ${bill} sir\n Thank you for visit :) ")
