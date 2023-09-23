import time
from player import Player

def printStringWithTime(string):
    for x in string:
        print(x, end = "")
        time.sleep(0.05)

def isDead(player1):
    if player1.hitpoints_current == 0:
        exit()
