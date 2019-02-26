# GURPS DUNGEON DOOR GENERATOR

# 1) Specify Max Tech Level
# 2) Specify how many doors you would like generated
# 3) Allow extra_heavy or vault doors?
# 4) Allow extra-heavy or vault security?
# 5) Allow locks?
# 6) Generate n number of doors and display output

# FUTURE IDEAS
# Add knots to security features
# Add traps
# Door Descriptions
# Generate key to go with locks
# Portcullis

import random

# door_type = {construction level:{DR:#, HP:#}, HT:#, ablative:boolean, TL:#}}
wood_door = {"name":"Wooden Door", "Light":{"DR":1, "HP":23}, "Average":{"DR":2, "HP":29}, "Heavy":{"DR":3, "HP":33}, "Extra Heavy":{"DR":6, "HP":42}, "Vault":{"DR":12, "HP":54}, "HT":12, "ablative":True, "TL":0}
ironbound_door = {"name":"Ironbound Wooden Door", "Light":{"DR":5, "HP":27}, "Average":{"DR":10, "HP":34}, "Heavy":{"DR":15, "HP":39}, "Extra Heavy":{"DR":30, "HP":49}, "Vault":{"DR":60, "HP":62}, "HT":12, "ablative":False, "TL":2}
iron_door = {"name":"Iron Door", "Light":{"DR":12, "HP":36}, "Average":{"DR":25, "HP":56}, "Heavy":{"DR":50, "HP":58}, "Extra Heavy":{"DR":75, "HP":66}, "Vault":{"DR":150, "HP":84}, "HT":12, "ablative":False, "TL":2}

# security_device = {construction level:{DR:#, HP:#}, HT:#, TL:#}
bolt = {"name":"Bolt", "Light":{"DR":3, "HP":6}, "Average":{"DR":6, "HP":9}, "Heavy":{"DR":9, "HP":18}, "Extra Heavy":{"DR":12, "HP":23}, "Vault":{"DR":24, "HP":46}, "HT":10, "TL":1}
latch = {"name":"Latch", "Light":{"DR":3, "HP":6}, "Average":{"DR":6, "HP":9}, "Heavy":{"DR":9, "HP":18}, "Extra Heavy":{"DR":12, "HP":23}, "Vault":{"DR":24, "HP":46}, "HT":10, "TL":2}
bar = {"name":"Bar", "Light":{"DR":1, "HP":14}, "Average":{"DR":2, "HP":18}, "Heavy":{"DR":4, "HP":23}, "Extra Heavy":{"DR":8, "HP":30}, "Vault":{"DR":16, "HP":37}, "HT":12, "TL":0}
wedge = {"name":"Wedge", "Light":{"DR":1, "HP":14}, "Average":{"DR":2, "HP":18}, "Heavy":{"DR":4, "HP":23}, "Extra Heavy":{"DR":8, "HP":30}, "Vault":{"DR":16, "HP":37}, "HT":12, "TL":0}

# Roll 3d6 and return the total.
def three_d_six():
	return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

# Returns a weighted random construction level of the object. If passed true, it will allow extra_heavy and vault levels.
def get_construction_level(allow_extreme):
	if allow_extreme == True:
		r = three_d_six()
		if r >= 17:
			level = "Vault"
		elif r <= 16 and r >= 15:
			level = "Extra Heavy"
		elif r <= 14 and r >= 12:
			level = "Heavy"
		elif r <= 11 and r >= 7:
			level = "Average"
		else:
			level = "Light"
	else:
		r = 18
		while r > 14:
			r = three_d_six()
		if r <= 14 and r >= 12:
			level = "Heavy"
		elif r <= 11 and r >= 7:
			level = "Average"
		else:
			level = "Light"
	return level

# Returns a weighted random door, including material and construction level.
def generate_door(TL, allow_extreme):	
	if TL >= 2:
		r = three_d_six()
		if r >= 15:
			return iron_door, get_construction_level(allow_extreme)
		elif r <= 8:
			return ironbound_door, get_construction_level(allow_extreme)
		else:
			return wood_door, get_construction_level(allow_extreme)
	else:
		return wood_door, get_construction_level(allow_extreme)

# Returns a random security device, including type and construction level.
def generate_security(TL, allow_extreme):
	list = [bar, wedge]
	if TL >= 1:
		list.append(bolt)
	if TL >= 2:
		list.append(latch)
	return random.choice(list), get_construction_level(allow_extreme)

# Returns a random lock type appropriate to the Tech Level and the corresponding Lockpicking modifier for that particular lock.
def generate_lock(TL):
	if TL == 0:
		# Knots will probably go here once implemented.
		return None, None
	locks = {"Cord and Bolt":[7, 8, 9], "Bolt and Tumbler":[6, 7, 8]}
	if TL >= 2:
		locks["Multiple Tumblers"] = [3, 4, 5]
		locks["Bolt and Barb-Spring"] = [1, 2, 3, 4]
		locks["Barb-Spring Padlock"] = [1, 2, 3, 4]
		locks["Rotary Lock"] = [1, 2, 3, 4]
	if TL >= 3:
		locks["Warded Rotary Lock"] = [-2, -1, 0, 1, 2, 3, 4]
	if TL >= 4:
		locks["Disc Combination Lock"] = [2, 3, 4]
		locks["Dial Combination Lock"] = [-2, -1, 0, 1, 2]
	lock = random.choice(locks.keys())
	return lock, random.choice(locks[lock])
	
def get_user_parameters():
	TL = input("What is the max Tech Level? ")
	extreme_door = raw_input("Allow extreme doors? (True/False) ")
	extreme_security = raw_input("Allow extreme security? (True/False) ")
	allow_locks = raw_input("Allow locks? (True/False) ")
	n = input("How many doors? ")
	return TL, n, bool(extreme_door), bool(extreme_security), bool(allow_locks)
	
TL, n, extreme_door, extreme_security, allow_locks = get_user_parameters()
for unused in range(0, n):
	
	# Get the type of door and how sturdy it is.
	door_type, door_level = generate_door(TL, extreme_door)
	
	# Get the security Device on the door and how sturdy it is.
	# Doors have a 2 in 5 chance of having a security device
	if random.randint(1, 5) <= 2:
		security_type, security_level = generate_security(TL, extreme_security)
	else:
		security_type, security_level = None, None
	
	# Generate a lock, but only if the security_type is a bolt or latch and allow_locks is true.
	if allow_locks == True and security_type != None:
		if security_type["name"] == "Bolt" or security_type["name"] == "Latch":
			lock_type, lockpick_mod = generate_lock(TL)
		else:
			lock_type, lockpick_mod = None, None
	else:
		lock_type, lockpick_mod = None, None

	# Generate output strings
	# Door output string
	if door_type["ablative"] == True:
		ablate = " Ablative"
	else:
		ablate = ""
	door_string = "Door: " + door_level + " " + door_type["name"] + " (DR: " + str(door_type[door_level]["DR"]) + ablate + ", HP: " + str(door_type[door_level]["HP"]) + ", HT: " + str(door_type["HT"]) + ", TL: " + str(door_type["TL"]) + ")"
	
	# Security output string
	if security_type != None:
		security_string = "  Security: " + security_level + " " + security_type["name"] + " (DR: " + str(security_type[security_level]["DR"]) + ", HP: " + str(security_type[security_level]["HP"]) + ", HT: " + str(security_type["HT"]) + ", TL: " + str(security_type["TL"]) + ")"
	
	# Lock output string
	if lock_type != None:
		if lockpick_mod >= 0:
			positive = "+"
		else:
			positive = ""
		lock_string = "  Lock: " + lock_type + " with " + positive + str(lockpick_mod) + " Lockpicking modifier"
	
	# Display the output
	print ""
	print door_string
	if security_type != None:
		print security_string
	if lock_type != None:
		print lock_string