import random

def roll_dice(dice):
    sum = 0
    critical = ""
    for unused in range(0, dice):
        sum = sum + random.randint(1,6)
    return sum

def quick_contest(target):
    roll, critical = roll_dice(3)
    return target - roll
