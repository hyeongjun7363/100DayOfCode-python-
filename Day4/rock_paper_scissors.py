import random

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

rock_paper_scissor = [rock, paper, scissors] 

player_choose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")
if player_choose == "0":
    player_choose = rock
elif player_choose == "1":
    player_choose = paper
elif player_choose == "2":
    player_choose = scissors

computer_choose = random.choice(rock_paper_scissor) # computer choosing randomly at rock_paper_scissors

print("Player choose: \n" + player_choose)
print("\n")
print("Computer choose: \n"+ computer_choose)


if player_choose == computer_choose: 
    print("draw") # if computer choosed and player choosed same, print 'draw'
elif (player_choose == rock and computer_choose == paper) or (player_choose == paper and computer_choose == scissors) or (player_choose == scissors and computer_choose == rock):
    print("computer win") # if computer win print 'computer win'
else:
    print("player win") # if player win print 'player win'