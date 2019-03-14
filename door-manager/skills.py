def forced_entry_skill():
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

def lockpicking_skill():
    while True:
        try:
            lockpicking = int(raw_input("Enter lockpicking skill: "))
        except ValueError:
            print "Input must be a number!"
            continue
        if lockpicking < 0:
            print "Input cannot be negative!"
            continue
        else:
            break
    return lockpicking

# Not really a skill, but it fits here code-wise
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
