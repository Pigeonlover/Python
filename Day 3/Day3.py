# AMUSEMENT PARK

print("Welcome to the rollercoaster ride!\n")

height = int(input("What is your height in cm?\n"))
age = int(input("What is your age?\n"))

if height > 120:
    print("Great, you can ride on the rollercoaster!")
    if age >= 18:
        print("You need to pay £12")
    elif age >= 12 and age < 18:
        print("You need to pay £7")
    else:
        print("Please pay £5")
else:
    print("Sorry! You are too short to ride on the rollercoaster.")




# Modulo operator '%' --> finds reminder to a division

print(10%3) # --> 1

number = int(input("Enter a random number:\n"))

if number%2 == 0:
    print("The number you entered is even!")
else:
    print("The number you entered is odd!")