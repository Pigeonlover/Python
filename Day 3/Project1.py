#ORDERING PIZZA PROGRAM

bill = 0

size = input("What size pizza would you like? Choose between S, M and L:\n")
if size == "S":
    bill += 10
elif size == "M":
    bill += 15
elif size == "L":
    bill += 20
else:
    print("Please only write either 'S', 'M' or 'L'!")

pepp = input("\nWould you like pepperoni added to your pizza? Y or N:\n")
if pepp == "Y" and size == "S":
    bill += 2
elif pepp == "Y" and size == "M":
    bill += 3
elif pepp == "Y" and size == "L":
    bill += 4

cheese = input("\nWould you like extra cheese on your pizza? Y or N:\n")
if cheese == "Y":
    bill += 1

print(f"\nGreat! Thank you for ordering with us. Your total bill comes up to:\n£{bill}")
