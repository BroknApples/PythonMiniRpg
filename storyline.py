import threading
from player import Player
from responses import *
from automation import *


def introduction():
    """Introduction to the game"""
    printStringWithTime("Hello Traveler. What is your name?\n")
    printStringWithTime("Enter your name: ")
    name = str(input())
    
    player1 = Player(name)
    
    thread2 = threading.Thread(target = isDead(player1))
    thread2.start()
    
    printStringWithTime(f"Hello {name}, my name is Rakshaska. I am The king of the Cheshire Empire. \n")
    printStringWithTime("You have been summoned to our world in order to defeat the demon king.\n\n")
    
    printStringWithTime("Choose a response:\n")
    introduction_response1()
    introduction_response2()
    introduction_response3()
    
    cont = True
    while cont == True:
        try:
            printStringWithTime("Enter 1, 2, or 3: ")
            choice = int(input())
            cont = False
        except:
            printStringWithTime("Invalid Input\n")
        
    
    if choice == 1:
        introduction_consequence1()
    elif choice == 2:
        introduction_consequence2()
    elif choice == 3:
        introduction_consequence3()
    
    
    