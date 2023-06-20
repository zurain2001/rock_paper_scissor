import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors. This game is a best of three.")
input("Press enter to continue ...")

rounds = 1
computer_score = 0
user_score = 0

while rounds < 4:
    print(f"round {rounds}")
    user_choice1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))
    if user_choice1 == 0:
        print("You chose Rock.")
        print(rock)
    elif user_choice1 == 1:
        print("You chose Paper.")
        print(paper)
    elif user_choice1 == 2:
        print("You chose Scissors.")
        print(scissors)
    else:
        print("Learn how to play then come back again.")
        sys.exit()

    computer_choice1 = random.randint(0, 2)

    if computer_choice1 == 0:
        print("Computer chose Rock.")
        print(rock)
    elif computer_choice1 == 1:
        print("Computer chose Paper.")
        print(paper)
    elif computer_choice1 == 2:
        print("Computer chose Scissors.")
        print(scissors)

    if computer_choice1 == 0 and user_choice1 == 2:
        print("Computer wins.")
        computer_score += 1
    elif user_choice1 == 0 and computer_choice1 == 2:
        print("You win.")
        user_score += 1

    elif computer_choice1 == 0 and user_choice1 == 1:
        print("You win.")
        user_score += 1
    elif user_choice1 == 0 and computer_choice1 == 1:
        print("Computer wins.")
        computer_score += 1

    elif computer_choice1 == 1 and user_choice1 == 2:
        print("You win.")
        user_score += 1
    elif user_choice1 == 1 and computer_choice1 == 2:
        print("Computer wins.")
        computer_score += 1

    elif user_choice1 == computer_choice1:
        print("It's a tie.")
    rounds += 1

if user_score > computer_score:
    print("You won the game.")
elif computer_score > user_score:
    print("Computer won the game.")
else:
    print("It's a tie.")