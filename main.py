import time
import threading
from enemies import *
from armor import *
from weapons import *
from player import *
from storyline import *
from automation import *


# Start game

def main():
    introduction()
    
thread1 = threading.Thread(target = main)
thread2 = threading.Thread(target = isDead)

thread1.start()
thread2.start()