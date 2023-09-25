import threading
from player import Player
from responses import *
from automation import *
from weapons import *
from armor import *
from enemies import *

# Choice variable
cont = True

def introduction():
    """Introduction to the game"""
    
    printStringWithTime("Hello Traveler. What is your name?\n")
    printStringWithTime("Enter your name: ")
    name = str(input())
    
    player1 = Player(name)
    
    thread2 = threading.Thread(target = isDead(player1))
    thread2.start()
    
    print("")
    
    
    # King speech
    
    printStringWithTime(f"Hello {name}, my name is Rakshaska. I am The king of the Cheshire Empire. \n")
    printStringWithTime("You have been summoned to our world in order to defeat the demon king.\n\n")
    
    printStringWithTime("Choose a response:\n")
    introduction_response1()
    introduction_response2()
    introduction_response3()
    
    
    
    choice = chooseOptions(cont, 3)
    
    if choice == 1:
        introduction_consequence1()
        
    elif choice == 2:
        introduction_consequence2()
        player1.hitpoints_current = 0
        isDead(player1)
        
    elif choice == 3:
        introduction_consequence3()
    
     
    
    # Recieve Weapon
    
    printStringWithTime("Choose a weapon:\n")
    starter_weapon()
    choice = chooseOptions(cont, 5)

    if choice == 1:
        stick = Sword(4, 0.10, 0.05, 0.00, 5)
        player1.equipped_weapon = stick
        
    elif choice == 2:
        long_stick = Polearm(2, -0.10, 0.10, 0.20, 5)
        player1.equipped_weapon = long_stick
        
    elif choice == 3:
        short_stick = Knife(2, 0.50, 0.05, 0.10, 5)
        player1.equipped_weapon = short_stick
        
    elif choice == 4:
        stick_with_string = Bow(4, -0.20, 0.25, 0.30, 5)
        player1.equipped_weapon = stick_with_string
        
    elif choice == 5:
        magic_stick = Staff(7, -0.45, 0.00, 0.15, 15)
        player1.equipped_weapon = magic_stick
        
    
    printStringWithTime("We have recently been getting our supplies cut off by the demons. Go to the\n")
    printStringWithTime("town of Celerity and kill the demon outposts near the town.\n\n")
    
    printStringWithTime("--You tell him you will make sure you get it done.\n\n")
    

def firstEncounterCelerity():
    printStringWithTime("YOU HAVE ENTERED CELERITY, THE SUPPLY TOWN")