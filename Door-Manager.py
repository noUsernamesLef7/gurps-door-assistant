# This file will be in charge of importing a door and keeping track of its status and health.

# Gets the doorstring from the user and returns a dictionary of the doors stats.
# Door string format: construction_level,material,DR,Ablative?,HP,HT,TL,security_construction_level,security_type,security_DR,security_HP,security_HT,security_TL,lock_type,lockpicking_modifier
def import_door():
	doorstring = raw_input("Enter the string of comma separated stats: ")
	door_stats = doorstring.split(',')
	door_stats_list = ["level", "material", "DR", "ablative", "HP", "HT", "TL", "security level", "security type", "security DR", "security HP", "security HT", "security TL", "lock type", "lockpicking modifier"]	
	door_dict = {}
	for i in range(0, len(door_stats_list)):
		if door_stats_list[i] in ["DR", "HP", "HT", "TL", "security DR", "security HP", "security HT", "security TL", "lockpicking modifier"]:
			door_dict[door_stats_list[i]] = int(door_stats[i])
		elif door_stats_list[i] == "ablative":
			door_dict[door_stats_list[i]] = bool(door_stats[i])
		else:
			door_dict[door_stats_list[i]] = door_stats[i]
	return door_dict

print import_door()
# Test String: Average,Wooden,2,True,29,12,0,Average,Bolt,6,9,10,1,Disc Combination,2
