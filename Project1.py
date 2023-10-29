import random

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
game_images = [Rock, Paper, Scissors]
print('Welcome to the game:-"Rock, Paper and Scissor"')
user_choice1 = int(input("what do you choose, type 0 for rock and 1 for paper and 2 for scissor"))
if user_choice1 >= 3 or user_choice1 < 0:
    print("you type an invalid number, you loose")
else:
    print(game_images[user_choice1])

    computer_choice = random.randint(0, 2)
    print("computer choose")
    print(game_images[computer_choice])

    if user_choice1 == 0 and computer_choice == 2:
        print("you won")
    elif computer_choice == 0 and user_choice1 == 2:
        print("you loose")
    elif computer_choice > user_choice1:
        print("you loose")
    elif computer_choice < user_choice1:
        print("you win")
    elif computer_choice == user_choice1:
        print("its draw")
