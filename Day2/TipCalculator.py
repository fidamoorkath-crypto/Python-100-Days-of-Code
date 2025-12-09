print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percentage = tip / 100
total_with_tip = bill * (1 + tip_percentage)
share_per_person = total_with_tip / people

print(f"Each person should pay: ${share_per_person:.2f}")
