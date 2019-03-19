import validation

# Gets the players forced entry skill bonus and returns the associated damage bonus.
def forced_entry_skill():
    while True:
        forced = raw_input("Is Forced Entry skill at DX+1 or DX+2? Enter 0, 1, or 2: ")
        if validation.is_valid_number(forced, False, True):
            if int(forced) < 3:
                break
        print "You must enter a number between 0 and 2!"
    return int(forced)

# Gets the players lockpicking skill and returns it.
def lockpicking_skill():
    while True:
        lockpicking = raw_input("Enter lockpicking skill level: ")
        if validation.is_valid_number(lockpicking, False, False):
            break
    return int(lockpicking)

# Gets the players strength and modifiers and returns the sum.
# ST is not really a skill, but it fits here code-wise.
def get_effective_strength():
    while True:
        st = raw_input("Enter ST: ")
        if validation.is_valid_number(st, False, True):
            break
    while True:
        modifiers = raw_input("Add relevant modifiers. Lifting ST, tools, etc: ")
        if validation.is_valid_number(modifiers, True, True):
            break
    return int(st) + int(modifiers)
