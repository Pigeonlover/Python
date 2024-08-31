# TIP CALCULATOR

total = float(input("How much is the total?\n£"))

tip = int(input("How much tip do you want to leave? Choose between 5, 10 or 15:\n%"))

people = int(input("And how many people are splitting the bill?\n"))

bill = (tip / 100 * total + total) / people

print(f"Each person needs to pay:\n£{round(bill, 2)}")
