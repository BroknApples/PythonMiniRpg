class Leather:
    """Leather armor stats"""
    def __init__(self, armor, dodge_chance, mana_catalyst, xp_growth, attribute):
        self.armor = 10
        self.dodge_chance = 10
        self.mana_catalyst = 0
        self.xp_growth = 1.15
        self.attribute = "none"
   
        
class Chainmail:
    """Chainmail armor stats"""
    def __init__(self, armor, dodge_chance, mana_catalyst, xp_growth, attribute):
        self.armor = 25
        self.dodge_chance = 0
        self.mana_catalyst = 0
        self.xp_growth = 1
        self.attribute = "physical_reduction"
        

class ApprenticeRobes:
    """Apprentice robes stats"""
    def __init__(self, armor, dodge_chance, mana_catalyst, xp_growth, attribute):
        self.armor = 5
        self.dodge_chance = 0
        self.mana_catalyst = 100
        self.xp_growth = 1.15
        self.attribute = "none"
        
        
class HighWizardRobes:
    """Apprentice robes stats"""
    def __init__(self, armor, dodge_chance, mana_catalyst, xp_growth, attribute):
        self.armor = 5
        self.dodge_chance = 0
        self.mana_catalyst = 100
        self.xp_growth = 1.35
        self.attribute = "magic_empowerment"
        
        
class RobesOfTheDead:
    """Robes of the dead stats"""
    def __init__(self, armor, dodge_chance, mana_catalyst, xp_growth, attribute):
        self.armor = 50
        self.dodge_chance = 15
        self.mana_catalyst = 200
        self.xp_growth = 1
        self.attribute = "necromancy"
        

class Netherite:
    """Netherite armor stats"""
    def __init__(self, armor, dodge_chance, mana_catalyst, xp_growth, attribute):
        self.armor = 175
        self.dodge_chance = 0
        self.mana_catalyst = 0
        self.xp_growth = 1
        
        
class Draconic:
    """Draconic armor stats"""
    def __init__(self, armor, dodge_chance, mana_catalyst, xp_growth, attribute):
        self.armor = 250
        self.dodge_chance = 25
        self.mana_catalyst = 500
        self.xp_growth = 1.25