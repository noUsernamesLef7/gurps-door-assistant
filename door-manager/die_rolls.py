import random

def roll_dice(dice):
    sum = 0
    critical = ""
    for unused in range(0, dice):
        sum = sum + random.randint(1,6)
    if sum == 18:
        critical = "failure"
    elif sum == 3 or sum == 4:
        critical = "success"
    return sum, critical

def quick_contest(target):
    roll, critical = roll_dice(3)
    return target - roll
