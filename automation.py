import time
from player import Player
from storyline import player1

def printStringWithTime(string):
    for x in string:
        print(x, end = "")
        time.sleep(0.05)

def isDead():
    if player1.hitpoints_current == 0:
        exit()
