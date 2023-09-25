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
thread1.start()