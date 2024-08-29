print("Welcome to this Pigeon Quiz!")

game = input("Are you interested in playing? ")
if game.lower() != "yes":
    print("Ok, bye!")
    quit()

print("Great! Ready?\n")

totalScore = 5

answer1 = input("QUESTION 1: How many legs does a pigeon have?")
if answer1 != "2":
    totalScore -= 1
    print("Wrong! Pigeons always have 2 legs!\n"); 
else : print("Correct!\n")

answer2 = input("QUESTION 2: How many years does a pigeon live on average in the wild?")
if answer2 != "5":
    totalScore -= 1
    print("Wrong! Pigeons only live around 5 years out there in the wild! It's a tough world...\n")
else : print("Correct!\n")

answer3 = input("QUESTION 3: How many eggs do pigeons lay in one clutch on average?")
if answer3 != "2":
    totalScore -= 1
    print("Wrong! Pigeons, on average, lay 2 eggs per nest!\n")
else : print("Correct!\n")

answer4 = input("QUESTION 4: Genetically, how many base colours exist in pigeons?")
if answer4 != "3":
    totalScore -= 1
    print("Wrong! Pigeons have 3 base colours: ash-red, blue and brown!\n")
else : print("Correct!\n")

answer5 = input("QUESTION 5: How many tail feathers do pigeons have?")
if answer5 != "12":
    totalScore -= 1
    print("Wrong! Pigeons have 12 tail feathers!\n")
else : print("Correct!\n")

print("Alright, the quiz is finished! You have found:")
print(totalScore,"/5 correct answers!")

print("\nThank you for playing. Bye!\n")
