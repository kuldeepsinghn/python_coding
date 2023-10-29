print("Welcome to the treasure island")
print("""*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'""")

print("Your mission to find the treasure")
choice1 = input('You are at the cross road, where do you want to go? type "left" or "right"')
if choice1 == "left":
    choice2 = input('there is a river in front of you, what do you want to go "swim or "wait"')
    if choice2 == "wait":
        #         game is continue
        choice3 = input('there is three door in front of you one is "red" if you want to chose "red" type"red",'
                        'another one is "blue" if you want to chose "blue" type"red", and last one is "yellow" if you '
                        'want to chose "yellow" type"yellow"')
        if choice3 == "red":
            print("the room red is full of fire so when you go inside it you will die")
        elif choice3 == "yellow":
            print("you found treasure, you won the game")
        elif choice3 == "blue":
            print("there are some wild rats they will kill you soon")
        else:
            print("you choose a door that doesn't exist")

    else:
        print("game over")
else:
    print("you fall into hole game over")
