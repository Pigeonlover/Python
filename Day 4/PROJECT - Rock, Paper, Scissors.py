# ROCK PAPER SCISSORS

import random

computer = random.randint(1, 3)


user = int(input("What move do you choose? Type 1 for Rock, 2 for Paper, 3 for Scissors:\n"))

print(f"You chose: {user}\n")
if user == 1:
   print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n\n''')
elif user == 2:
   print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\n\n''')
elif user == 3:
   print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n\n''')


print(f"The computer chose: {computer}\n")
if computer == 1:
   print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n\n''')
elif computer == 2:
   print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
\n\n''')
elif computer == 3:
   print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n\n''')


if user == 1 and computer == 3:
   print("RESULT: You win!\n\n")
elif computer > user:
   print("RESULT: You lose!\n\n")

