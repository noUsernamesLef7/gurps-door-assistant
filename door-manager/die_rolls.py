import random

# Takes an integer and rolls that many dice, returning the sum.
def roll_dice(dice):
    sum = 0
    critical = ""
    for unused in range(0, dice):
        sum = sum + random.randint(1,6)
    return sum

# Takes a target number and rolls a quick contest against it.
def quick_contest(target):
    roll, critical = roll_dice(3)
    return target - roll
