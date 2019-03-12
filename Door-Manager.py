import door
import random

# Gets the doorstring from the user and returns a new door object.
# Door string format: construction_level,material,DR,Ablative?,HP,HT,TL,security_construction_level,security_type,security_DR,security_HP,security_HT,security_TL,lock_type,lockpicking_modifier
def import_door():
	doorstring = raw_input("Enter the string of comma separated stats: ")
	door_stats = doorstring.split(',')
        new_door = door.Door(door_stats)
        return new_door

def roll_dice(dice):
    sum = 0
    for unused in range(0, dice):
        sum = sum + random.randint(1,6)
    return sum

def quick_contest(target):
    return target - roll_dice(3)
    

def all_out_attack(dice):
    if raw_input("Is this an all-out-attack? yes/no ") == "yes":
        if dice > 2:
            return dice
        else:
            return 2
    return 0

def forced_entry():
    forced = input("Is Forced Entry skill at DX+1 or DX+2 plus? 0/1/2  ")
    if forced == 1 or forced == 2:
        return forced
    else:
        return 0

def get_damage():
    return input("How many dice of damage? "), input("What is the damage modifier? ")

def get_effective_strength():
    return input("Enter ST: ") + input("Lifting ST bonus, if applicable: ") + input("Add any other relevant modifiers, tools, etc: ")

def crush_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + forced_entry()
    damage = roll_dice(dice) + modifier - door.dr
    door.do_damage(damage)
    print "You deal " + str(damage) + " crushing damage to the door!\n" 

def cut_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + forced_entry()
    # Cutting attacks multiply damage by 1.5
    damage = (roll_dice(dice) + modifier - door.dr) * 1.5
    damage = int(round(damage))
    door.do_damage(damage)
    print "You deal " + str(damage) + " cutting damage to the door!\n"

def force_door(door):
    # TODO If device is a wedge or bar, the door can break before the security feature. Code should reflect this.
    attacker_margin = quick_contest(get_effective_strength() + forced_entry() - door.security_dr)
    defender_margin = quick_contest(door.security_hp)
    print "Margin: " + str(attacker_margin) + " Door Margin: " + str(defender_margin)
    if attacker_margin > defender_margin:
        door.secured = False
    else:
        print "The door remains fastly shut!\nNext attempt, subtract 1 from ST and lose 1 FP.\n"

def pick_lock(door):
    skill = input("Lockpicking skill? ")
    margin = skill + door.lockpicking_modifier - roll_dice(3)
    if margin > 0:
        seconds = 60 - (margin * 5)
        if seconds < 10:
            seconds = 10
        print "You spend " + str(seconds) + " seconds picking the lock."
        door.picked = True
    else:
        print "You waste a full minute fumbling around with the lock."

def do_action(door):
    print "Door HP: " + str(door.hp) + " Door DR: " + str(door.dr)
    print "1 - Crushing Attack\n2 - Cutting Attack"
    if door.secured:
        print "3 - Force Door Open"
    if door.locked:
        print "4 - Pick Lock"
    action = input("Enter the number of desired action: ")
    if action == 1:
        crush_attack(door)
    elif action == 2:
        cut_attack(door)
    elif door.secured and action == 3:
        force_door(door)
    elif door.locked and action == 4:
        pick_lock(door)
    else:
        print action + " is an invalid input"

# Test String: Average,Wooden,2,True,29,12,0,Average,Bolt,6,9,10,1,Disc Combination, -1
# Main loop
door = import_door()
while not door.broken and not door.forced and not door.picked:
    do_action(door)
    door.update_state()
if door.broken:
    print "The door breaks open!"
elif door.forced:
    print "\nThe door is forced open!"
else:
    print "\nThe door swings open!"
