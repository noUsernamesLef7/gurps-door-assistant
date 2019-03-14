import door
import attack
import actions

# Gets the doorstring from the user and returns a new door object.
# Format: construction_level,material,DR,Ablative?,HP,HT,TL,security_construction_level,security_type,security_DR,security_HP,security_HT,security_TL,lock_type,lockpicking_modifier
def import_door():	
    door_stats = []
    while len(door_stats) != 15:
        doorstring = raw_input("Enter the string of comma separated stats: ")
        door_stats = doorstring.split(',')
        if len(door_stats) != 15:
            print "Invalid import string!"
    new_door = door.Door(door_stats)
    return new_door

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
        attack.crush_attack(door)
    elif action == 2:
        attack.cut_attack(door)
    elif action == 3:
        actions.force_door(door)
    elif action == 4:
        actions.pick_lock(door)

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
