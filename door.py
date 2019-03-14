import random

class Door:
    def __init__(self, door_stats):
        self.level = door_stats[0]
        self.material = door_stats[1]
        self.dr = int(door_stats[2])
        self.ablative = bool(door_stats[3])
        self.max_hp = int(door_stats[4])
        self.hp = int(door_stats[4])
        self.ht = int(door_stats[5])
        self.tl = int(door_stats[6])
        if door_stats[8] != "n/a":
            self.security_level = door_stats[7]
            self.security_type = door_stats[8]
            self.security_dr = int(door_stats[9])
            self.security_hp = int(door_stats[10])
            self.security_ht = int(door_stats[11])
            self.security_tl = int(door_stats[12])
            self.secured = True
            if door_stats[13] != "n/a":
                self.lock_type = door_stats[13]
                self.lockpicking_modifier = int(door_stats[14])
                self.locked = True
            else:
                self.locked = False
        else:
            self.secured = False
            self.locked = False
        self.picked = False
        self.forced = False
        self.broken = False
        self.update_state()

    def do_damage(self, damage):
        self.hp = self.hp - damage
        if self.ablative and self.dr != 0:
            self.dr = self.dr - damage
            if self.dr < 1:
                self.dr = 1

    def update_state(self):
        if self.hp < 0:
            if random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) > self.ht:
                self.broken = True
        if self.hp < -5 * self.max_hp:
            self.broken = True
