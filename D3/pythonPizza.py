print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ").lower().strip()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower().strip()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower().strip()

total = 0  

if size == 's':
    total = 15
    if pepperoni == 'y':
        total += 2
    if extra_cheese == 'y':
        total += 1

elif size == 'm':
    total = 20
    if pepperoni == 'y':
        total += 3
    if extra_cheese == 'y':
        total += 1

elif size == 'l':
    total = 25
    if pepperoni == 'y':
        total += 3
    if extra_cheese == 'y':
        total += 1

else:
    print("Invalid size selected.")

print(f"Your final bill is: ${total}")
