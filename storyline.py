from player import Player
from responses import *


def introduction():
    """Introduction to the game"""
    print("Hello Traveler. What is your name?")
    name = str(input("My name is "))
    print (".")
    
    player1 = Player(name)
    
    print(f"Hello {name}, my name is Rakshaska. I am The king of the Cheshire Empire. \n")
    print("You have been summoned to our world in order to defeat the demon king. ")
    
    print("Choose a response:\n")
    introduction_response1()
    introduction_response2()
    introduction_response3()
    choice = int(input())
    
    
    
    