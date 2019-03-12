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

def all_out_attack(dice, modifier):
    if raw_input("Is this an all-out-attack? yes/no ") == "yes":
        if dice > 2:
            return modifier + dice
        else:
            return modifier + 2

def get_damage():
    dice = input("How many dice of damage? ")
    modifier = input("What is the damage modifier? ")
    return dice, modifier

def crush_attack(door):
    dice, modifier = get_damage()
    modifier = all_out_attack(dice, modifier)
    damage = roll_dice(dice) + modifier - door.dr
    door.do_damage(damage)
    print "You deal " + str(damage) + " crushing damage to the door!\n" 

def cut_attack(door):
    dice, modifier = get_damage()
    modifier = all_out_attack(dice, modifier)
    # Cutting attacks multiply damage by 1.5
    damage = (roll_dice(dice) + modifier - door.dr) * 1.5
    damage = int(round(damage))
    door.do_damage(damage)
    print "You deal " + str(damage) + " cutting damage to the door!\n"

def do_action(door):
    print "Door HP: " + str(door.hp) + " Door DR: " + str(door.dr)
    print "1 - Crushing Attack"
    print "2 - Cutting Attack"
    action = input("Enter the number of desired action: ")
    if action == 1:
        crush_attack(door)
    elif action == 2:
        cut_attack(door)
    else:
        print action + " is an invalid input"

# Test String: Average,Wooden,2,True,29,12,0,Average,Bolt,6,9,10,1,Disc Combination, -1
# Main loop
door = import_door()
while not door.broken:
    do_action(door)
    door.update_state()
print "The door breaks open!"
