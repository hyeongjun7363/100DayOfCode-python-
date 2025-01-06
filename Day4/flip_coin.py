import random

def flip_the_coin():
    flip_coin = random.randint(0, 1)
    if flip_coin == 0:
        print("Heads")
    else:
        print("Tails")