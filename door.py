class Door:
    def __init__(self, door_stats):
        self.level = door_stats[0]
        self.material = door_stats[1]
        self.dr = int(door_stats[2])
        self.ablative = bool(door_stats[3])
        self.hp = int(door_stats[4])
        self.ht = int(door_stats[5])
        self.tl = int(door_stats[6])
        self.security_level = door_stats[7]
        self.security_type = door_stats[8]
        self.security_dr = int(door_stats[9])
        self.security_hp = int(door_stats[10])
        self.security_ht = int(door_stats[11])
        self.security_tl = int(door_stats[12])
        self.lock_type = door_stats[13]
        self.lockpicking_modifier = int(door_stats[14])

    def do_damage(self, damage):
        self.hp = self.hp - damage
