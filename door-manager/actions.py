import die_rolls
import skills

def force_door(door):
    attacker_margin = die_rolls.quick_contest(skills.get_effective_strength() + skills.forced_entry_skill() - door.security_dr)
    defender_margin = die_rolls.quick_contest(door.security_hp)
    if attacker_margin > defender_margin:
        print "The force destroys the " + door.security_type + "!"
        door.secured = False
    else:
        print "You fail the check by " + str(defender_margin - attacker_margin) + " and the " + door.material + " remains fastly shut!\nNext attempt, subtract 1 from ST and lose 1 FP."

def pick_lock(door):
    skill = skills.lockpicking_skill()
    roll, critical = die_rolls.roll_dice(3)
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
