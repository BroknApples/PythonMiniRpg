import time
import sys

def printStringWithTime(string):
    for x in string:
        print(x, end = "")
        time.sleep(0.05)

def isDead(player1):
    if player1.hitpoints_current == 0:
        sys.exit()
        
def chooseOptions(cont, num):
    while cont == True:
        i = 1
        while i <= num:
            if i == 1:
                printStringWithTime("Enter ")
                
            if i < (num - 1):
                printStringWithTime(f"{i}, ")
            elif i == (num - 1):
                printStringWithTime(f"{i}, or ")
            elif i == num:
                printStringWithTime(f"{i}: ")
                
            i += 1
        try:
            choice = int(input())
            cont = False
        except:
            printStringWithTime("Invalid Input\n")
    cont = True
    
    return choice
