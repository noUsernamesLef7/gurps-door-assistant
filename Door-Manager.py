import door
import random

# Gets the doorstring from the user and returns a new door object.
# Door string format: construction_level,material,DR,Ablative?,HP,HT,TL,security_construction_level,security_type,security_DR,security_HP,security_HT,security_TL,lock_type,lockpicking_modifier
def import_door():	
    door_stats = []
    while len(door_stats) != 15:
        doorstring = raw_input("Enter the string of comma separated stats: ")
        door_stats = doorstring.split(',')
        if len(door_stats) != 15:
            print "Invalid import string!"
    new_door = door.Door(door_stats)
    return new_door

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

def all_out_attack(dice):
    all_out = ""
    while True: 
        all_out = raw_input("Is this an all-out-attack? ")
        if all_out == "yes" or all_out == "no":
            break
        print "Response must be 'yes' or 'no'."
    if all_out == "yes":
        if dice > 2:
            return dice
        else:
            return 2
    return 0

def forced_entry():
    while True:
        try:
            forced = int(raw_input("Is Forced Entry skill at DX+1 or DX+2 plus? Enter 0, 1, or 2:  "))
        except ValueError:
            print "Input must be a number!"
            continue
        if forced in [0, 1, 2]:
            break
        print "You must enter an number between 0 and 2!"
    if forced == 1 or forced == 2:
        return forced
    else:
        return 0

def get_damage():
    while True:
        try:
            dice = int(raw_input("How many dice of damage? "))
        except ValueError:
            print "Input must be a number!"
            continue
        if dice > 0:
            break
        print "The number must be at least 1!"
    while True:
        try:
            modifier = int(raw_input("What is the damage modifier? "))
        except ValueError:
            print "Input must be a number!"
        else:
            break
    return dice, modifier

def get_effective_strength():
    while True:
        try:
            st = int(raw_input("Enter ST: "))
        except ValueError:
            print "Input must be a number!"
            continue
        if st >= 0:
            break
        print "ST cannot be negative!"
    while True:
        try:
            modifiers = int(raw_input("Add relevant modifiers. Lifting ST, tools, etc: "))
        except ValueError:
            print "Input must be a number!"
        else:
            break
    return st + modifiers

def crush_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + forced_entry()
    roll, critical = roll_dice(dice)
    damage = roll + modifier - door.dr
    if critical == "failure":
        print "Critical failure!\nThe result is up to the GM's imagination."
    if critical == "success":
        print "Critical success!\nConsult the Critical Hit Table.\nBase damage is " + str(damage) + "."
    else:
        door.do_damage(damage)
        print "You deal " + str(damage) + " crushing damage to the " + door.material + "!"

def cut_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + forced_entry()
    roll, critical = roll_dice(dice)
    # Cutting attacks multiply damage by 1.5
    damage = int(round((roll + modifier - door.dr) * 1.5))
    if critical == "failure":
        print "Critical failure!\nThe result is up to the GM's imagination."
    elif critical == "success":
        print "Critical success!\nConsult the Critical Hit Table.\nBase damage is " + str(damage) + "."
    else:
        door.do_damage(damage)
        print "You deal " + str(damage) + " cutting damage to the " + door.material + "!"

def force_door(door):
    attacker_margin = quick_contest(get_effective_strength() + forced_entry() - door.security_dr)
    defender_margin = quick_contest(door.security_hp)
    if attacker_margin > defender_margin:
        print "The force destroys the " + door.security_type + "!"
        door.secured = False
    else:
        print "You fail the check by " + str(defender_margin - attacker_margin) + " and the " + door.material + " remains fastly shut!\nNext attempt, subtract 1 from ST and lose 1 FP."

def pick_lock(door):
    skill = input("Lockpicking skill? ")
    roll, critical = roll_dice(3)
    if critical == "failure":
        print "Uh oh. You seem to have jammed the " + door.lock_type + " closed."
        door.locked = False
        return
    elif critical == "success":
        print "You skillfully pick the " + door.lock_type + " in only 15 seconds!"
        door.picked = True
    elif skill + door.lockpicking_modifier - roll > 0:
        seconds = 60 - ((skill + door.lockpicking_modifier - roll) * 5)
        if seconds < 10:
            seconds = 10
        print "You spend " + str(seconds) + " seconds picking the " + door.lock_type + "."
        door.picked = True
    else:
        print "You waste a full minute fumbling around with the " + door.lock_type + "."

def do_action(door):
    while True:
        print "\n" + door.level + " " + door.material + "\nHP: " + str(door.hp) + " DR: " + str(door.dr)
        if door.secured:
            print door.security_level + " " + door.security_type + "\nHP: " + str(door.security_hp) + " DR: " + str(door.security_dr)
        if door.locked:
            print door.lock_type + " (Modifier: " + str(door.lockpicking_modifier) + ")"
        print "1 - Crushing Attack\n2 - Cutting Attack"
        if door.secured:
            print "3 - Force Door Open"
        if door.locked:
            print "4 - Pick Lock"
        try:
            action = int(raw_input("Enter the number of desired action: "))
        except ValueError:
            print "You must enter a number!"
            continue
        if action > 4:
            print "Not a valid option!"
        elif action == 3 and not door.secured:
            print "Not a valid option!"
            continue
        elif action == 4 and not door.locked:
            print "Not a valid option!"
            continue
        else:
            break
    if action == 1:
        crush_attack(door)
    elif action == 2:
        cut_attack(door)
    elif action == 3:
        force_door(door)
    elif action == 4:
        pick_lock(door)

# Test String: Average,Wooden,2,True,29,12,0,Average,Bolt,6,9,10,1,Disc Combination, -1
# Main loop
door = import_door()
while not door.broken and not door.forced and not door.picked:
    do_action(door)
    door.update_state()
if door.broken:
    print "The " + door.material + " breaks open!"
elif door.forced:
    print "\nThe " + door.material + " is forced open!"
else:
    print "\nThe " + door.material + " swings open!"
