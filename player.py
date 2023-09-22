from storyline import *
class Player:
    """User controlled character"""
    def __init__(self, name, level, xpCount, enemies_killed, hitpoints, attack_damage, armor, dodge_chance, crit_chance, crit_damage): 
    self.name = name
    self.level = level
    self.xpCount = xpCount
    self.enemies_killed = enemies_killed
    self.hitpoints = hitpoints
    self.attack_damage = attack_damage
    self.armor = armor
    self.dodge_chance = dodge_chance
    self.crit_chance = crit_chance
    self.crit_damage = crit_damage