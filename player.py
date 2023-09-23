class Player:
    """User controlled character"""
    def __init__(self, name): 
        self.name = name
        self.level = 1
        self.xpCount = 0
        self.enemies_killed = 0
        self.hitpoints_max = 10
        self.hitpoints_current = 10
        self.attack_damage = 2
        self.attack_speed = 1.00
        self.mana = 5
        self.armor = 2
        self.dodge_chance = 0.00
        self.crit_chance = 0.00
        self.crit_damage = 0.45
        self.equipped_weapon = "none"
        self.equipped_armor = "none"