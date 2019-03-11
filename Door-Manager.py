import door

# Gets the doorstring from the user and returns a new door object.
# Door string format: construction_level,material,DR,Ablative?,HP,HT,TL,security_construction_level,security_type,security_DR,security_HP,security_HT,security_TL,lock_type,lockpicking_modifier
def import_door():
	doorstring = raw_input("Enter the string of comma separated stats: ")
	door_stats = doorstring.split(',')
        new_door = door.Door(door_stats)
        return new_door

print import_door()
# Test String: Average,Wooden,2,True,29,12,0,Average,Bolt,6,9,10,1,Disc Combination, -1
