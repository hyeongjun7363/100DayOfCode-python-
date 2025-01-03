print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
LR_way = input("You're at a cross road. Where do you want to go?\n    Type" + ''' "left" or "right" \n''')
if LR_way == "left":
    going_lack = input("You've come to a lack. There is an island in the middle of the lack. \n     Type " + '''"wait" to wait for a boat. Type "swim" to swim across.\n''')
    if going_lack == "wait":
        choose_color = input("You arrive at the island unharmed. There is a house wih 3 doors.\n  One red, one yellow and one blue. Which clour do you choose.\n")
        if choose_color == "red":
            print("Burned by fire. Game Over.")
        elif choose_color == "yellow":
            print("You find the treasure. You win!")
        elif choose_color == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("You chose wrong. Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game over!")