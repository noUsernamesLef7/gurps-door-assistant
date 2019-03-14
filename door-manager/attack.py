import skills
import die_rolls

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

def cut_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + skills.forced_entry_skill()
    roll, critical = die_rolls.roll_dice(dice)
    # Cutting attacks multiply damage by 1.5
    damage = int(round((roll + modifier - door.dr) * 1.5))
    if critical == "failure":
        print "Critical failure!\nThe result is up to the GM's imagination."
    elif critical == "success":
        print "Critical success!\nConsult the Critical Hit Table.\nBase damage is " + str(damage) + "."
    else:
        door.do_damage(damage)
        print "You deal " + str(damage) + " cutting damage to the " + door.material + "!"

def crush_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + skills.forced_entry_skill()
    roll, critical = die_rolls.roll_dice(dice)
    damage = roll + modifier - door.dr
    if critical == "failure":
        print "Critical failure!\nThe result is up to the GM's imagination."
    if critical == "success":
        print "Critical success!\nConsult the Critical Hit Table.\nBase damage is " + str(damage) + "."
    else:
        door.do_damage(damage)
        print "You deal " + str(damage) + " crushing damage to the " + door.material + "!"
