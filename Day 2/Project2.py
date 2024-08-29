import random

x = random.randrange(1, 11)

print("Guess The Number!\n")
number = input("I'm thinking of... A number between 1 and 10. Can you guess it?\n")

if number.isdigit():
    number = int(number)
    if number <= 0:
        print("Please enter only numbers above 0, thank you.\n")
        quit()
else : 
    print("Please enter only full numbers!\n")
    quit()

if x == number:
    print("Congratulations! You guessed the number right!")
    quit()
else :
    print("Sorry, the number was", x,"instead!")
    quit()
