# This script works when the user is facing 0 degrees on the y axis and either -46.5 degrees
# or 133.5 degrees on the x axis. Speed should be set at 327 with rancher boots.
# 200 speed boots for cactus at straight 90 degrees.
# 116 speed boots for nether wart at straight 90 degrees.

import pyautogui as pag
from time import sleep
import random
import time
import keyboard
import sys

class Hypixel:

    def __init__(self) -> None:
        self.sugar_cane_rows = 32
        self.cactus_rows = 14
        self.nether_wart_rows = 18
    
    def prompt(self):
        print("Please enter the corrisponding number for which script you would like to run:")
        print("1: Sugarcane Script")
        print("2: Cactus Script")
        print("3: Nether Wart Script")

        while True:
            ans = input("Enter here: ")
            
            if ans == "1":
                Hypixel.sugar_cane()
                break
            elif ans == "2":
                Hypixel.cactus()
                break
            elif ans == "3":
                Hypixel.nether_wart()
                break
            else:
                print("Invalid input. Try again.")
                continue

    def sleep_with_pause(self, duration):
        """Sleeps for the specified duration, but checks for pause every 0.1 seconds."""
        end_time = time.time() + duration
        while time.time() < end_time:
            if keyboard.is_pressed(']'):
                return True
            time.sleep(0.1)
        return False

    def sugar_cane(self):
        time.sleep(3)

        is_paused = True
        
        while True:
            if keyboard.is_pressed(']'):
                is_paused = not is_paused
                print("Paused" if is_paused else "Resumed")
                time.sleep(1)

            if not is_paused:
                x = 0
                pag.mouseDown()
                while x <= self.sugar_cane_rows - 2:
                    # Generate new number
                    time_to_walk_row = random.uniform(9.525,9.567)

                    # Debug
                    print(time_to_walk_row)
                    print(x)

                    # Walk Right
                    pag.keyDown('d')
                    if self.sleep_with_pause(time_to_walk_row):
                        pag.keyUp('d')
                        break
                    pag.keyUp('d')
                    
                    if x < self.sugar_cane_rows - 2:
                        # Walk Left
                        pag.keyDown('s')
                        if self.sleep_with_pause(time_to_walk_row + 0.225):
                            pag.keyUp('s')
                            break
                        pag.keyUp('s')

                    x = x + 2
                pag.mouseUp()

                print("Farming complete.")
                restart = input("Would you like to restart? (y/n): ")
                if restart == "y":
                    print("Restarting...")
                    Hypixel.sugar_cane()
                elif restart == "n":
                    print("Closing script...")
                    sys.exit()
    
    def cactus(self):
        time.sleep(3)

        is_paused = True
        
        while True:
            if keyboard.is_pressed(']'):
                is_paused = not is_paused
                print("Paused" if is_paused else "Resumed")
                time.sleep(1)

            if not is_paused:
                x = 0
                pag.mouseDown()
                pag.keyDown('s')
                while x <= self.cactus_rows - 2:
                    # Generate new number
                    time_to_walk_row = random.uniform(15.01,15.05)

                    # Debug
                    print(time_to_walk_row)
                    print(x)

                    if x > 0:
                        time.sleep(1.25)
                    # Walk Right
                    pag.keyDown('d')
                    if self.sleep_with_pause(time_to_walk_row):
                        pag.keyUp('d')
                        break
                    pag.keyUp('d')

                    time.sleep(1.25)
                    
                    if x < self.cactus_rows - 2:
                        # Walk Left
                        pag.keyDown('a')
                        if self.sleep_with_pause(time_to_walk_row):
                            pag.keyUp('a')
                            break
                        pag.keyUp('a')

                    x = x + 2
                pag.mouseUp()
                pag.keyUp('s')

                print("Farming complete.")
                restart = input("Would you like to restart? (y/n): ")
                if restart == "y":
                    print("Restarting...")
                    Hypixel.cactus()
                elif restart == "n":
                    print("Closing script...")
                    sys.exit()

    def nether_wart(self):
        time.sleep(3)

        is_paused = True
        
        while True:
            if keyboard.is_pressed(']'):
                is_paused = not is_paused
                print("Paused" if is_paused else "Resumed")
                time.sleep(1)

            if not is_paused:
                x = 0
                pag.mouseDown()
                while x <= self.nether_wart_rows - 2:
                    # Generate new number
                    time_to_walk_row = random.uniform(18.1,18.15)

                    # Debug
                    print(time_to_walk_row)
                    print(x)

                    # Walk Right
                    pag.keyDown('d')
                    if self.sleep_with_pause(time_to_walk_row):
                        pag.keyUp('d')
                        break
                    pag.keyUp('d')

                    # Walk Forward
                    pag.keyDown('w')
                    if self.sleep_with_pause(0.97):
                        pag.keyUp('w')
                        break
                    pag.keyUp('w')

                    # Walk Left
                    pag.keyDown('a')
                    if self.sleep_with_pause(time_to_walk_row):
                        pag.keyUp('a')
                        break
                    pag.keyUp('a')
                    
                    if x < self.nether_wart_rows - 2:
                        # Walk Forward
                        pag.keyDown('w')
                        if self.sleep_with_pause(0.97):
                            pag.keyUp('w')
                            break
                        pag.keyUp('w')

                    x = x + 2
                pag.mouseUp()

                print("Farming complete.")
                restart = input("Would you like to restart? (y/n): ")
                if restart == "y":
                    print("Restarting...")
                    Hypixel.nether_wart()
                elif restart == "n":
                    print("Closing script...")
                    sys.exit()



if __name__ == '__main__':
    Hypixel = Hypixel()
    Hypixel.prompt()
