import time
import enemies
import armor
import weapons

'''
Create a mini-rpg with upgradeable character

Character Items:

    Swords:
        Stick
        Blunt Sword
        Sharp Stick
        Blade of the Shadows
        Excalibur

    Polearms:
        Long Stick
        Basic Polearm
        Guard's Polearm
        Spear of Shojin
        Wukong's Polearm

    Knives:
        Short Stick
        Kitchen Knife
        Kunai
        Shadow Knife
        
    Bows/Crossbows:
        Stick with a String
        Longbow
        Basic Crossbow
        Crossbow of Death
        Runaan's Hurricane
        
    Staffs:
        Stick of Magic
        Basic Staff
        Necromancer's Staff
        Wizard King's Staff

    Armor:
        Leather Armor
        Chainmail Armor
        Apprentice Robes
        Robes of the Dead
        High Wizard Robes
        Netherite Armor


 Neutral Enemies(Portrayed as evil, but is friendly unless provoked):
 
 Wind Dragon of the North
 Earth Dragon of the South
 Fire Dragon of the East
 Water Dragon of the West
 
 Boar
 Bull
 Fireflies
'''

def introduction():
    print("Hello Traveler. What is your name?")
    name = str(input("My name is "))
    print (".")
    
    print("Hello " + name + ", my name is Rakshaska. I am The king of the Cheshire Empire.\n")