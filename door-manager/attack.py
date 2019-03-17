import skills
import die_rolls
import validation

def get_damage():
    while True:
        dice = raw_input("How many dice of damage? ")
        if validation.is_valid_number(dice, False, False):
            break
    while True:
        modifier = raw_input("What is the damage modifier? ")
        if validation.is_valid_number(modifier, True, True):
            break
    return int(dice), int(modifier)

def all_out_attack(dice):
    all_out = ""
    while True:
        all_out = raw_input("Is this an all-out-attack? (True/False) ")
        if validation.is_valid_boolean(all_out):
            break
    if bool(all_out):
        if dice > 2:
            return dice
        else:
            return 2
    return 0

def cut_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + skills.forced_entry_skill()
    roll = die_rolls.roll_dice(dice)
    # Cutting attacks multiply damage by 1.5
    damage = int(round((roll + modifier - door.dr) * 1.5))
    if roll == 18:
        print "Critical failure!\nThe result is up to the GM's imagination."
    elif roll == 3 or roll == 4:
        print "Critical success!\nConsult the Critical Hit Table.\nBase damage is " + str(damage) + "."
    else:
        door.do_damage(damage)
        print "You deal " + str(damage) + " cutting damage to the " + door.material + "!"

def crush_attack(door):
    dice, modifier = get_damage()
    modifier = modifier + all_out_attack(dice) + skills.forced_entry_skill()
    roll, critical = die_rolls.roll_dice(dice)
    damage = roll + modifier - door.dr
    if roll == 18:
        print "Critical failure!\nThe result is up to the GM's imagination."
    if roll == 3 or roll == 4:
        print "Critical success!\nConsult the Critical Hit Table.\nBase damage is " + str(damage) + "."
    else:
        door.do_damage(damage)
        print "You deal " + str(damage) + " crushing damage to the " + door.material + "!"
