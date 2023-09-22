from storyline import name
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
        self.mana = 5
        self.armor = 2
        self.dodge_chance = 0
        self.crit_chance = 0
        self.crit_damage = 45