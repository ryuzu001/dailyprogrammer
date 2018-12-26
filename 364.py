# https://redd.it/8s0cy1
import random

def roll_dice(sides):
    return random.randint(0, sides)

user_dice = input("Enter a number of dice to roll (and sides) in the form NdM (ie. 3d6): ")
rolls = user_dice.split("d")
if not len(rolls) == 2:
    print("Input error")
    exit()
if not rolls[0].isdigit() or not rolls[1].isdigit():
    print("Parse error")
    exit()
num_rolls = int(rolls[0])
num_sides = int(rolls[1])
x = 0
for i in range(0, num_rolls):
    x += roll_dice(num_sides)
print("Your number is " + str(x))