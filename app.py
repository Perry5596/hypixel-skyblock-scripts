# Custom TKInter documentation: https://customtkinter.tomschimansky.com/

# SCRIPT NOTES:
# Nether Wart: 90 degrees x, 0-1 degrees y, 116 speed
# Sugar Cane: 133.5 degrees x, 0 degrees y, 327 speed
# Cactus: 90 degreess x, 0 degrees y, 200 speed

import customtkinter
import time
import keyboard
import pyautogui as pag
import random
import sys


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure system properties
        customtkinter.set_appearance_mode("dark")

        # configure window
        self.title("Hypixel Farming Scripts")
        self.geometry(f"{350}x{500}")
        self.resizable(False, False)

        # WIDGETS

        # title
        self.logo_label = customtkinter.CTkLabel(
            self, text="Farming Scripts", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=60, pady=25)

        # select script
        self.select_label = customtkinter.CTkLabel(
            self, text="Select Script", font=customtkinter.CTkFont(size=18))
        self.select_label.grid(row=1, column=0, padx=100, pady=5)

        self.selection_menu = customtkinter.CTkOptionMenu(
            self, values=["Nether Wart", "Sugar Cane", "Cactus"])
        self.selection_menu.grid(row=2, column=0, padx=100, pady=5)

        # select amount of farming rows
        self.select_label = customtkinter.CTkLabel(
            self, text="Amount of Rows", font=customtkinter.CTkFont(size=18))
        self.select_label.grid(row=3, column=0, padx=100, pady=5)

        self.farming_rows = customtkinter.CTkEntry(
            self, placeholder_text="number here")
        self.farming_rows.grid(row=4, column=0, padx=100, pady=5)

        # play pause keybind
        self.play_pause_label = customtkinter.CTkLabel(
            self, text="Play/Pause Keybind", font=customtkinter.CTkFont(size=18))
        self.play_pause_label.grid(row=5, column=0, padx=100, pady=5)

        self.play_pause_keybind = customtkinter.CTkEntry(
            self, placeholder_text="single key here")
        self.play_pause_keybind.grid(row=6, column=0, padx=100, pady=5)

        # run button

        self.run_button = customtkinter.CTkButton(
            self, text="Run Script", font=customtkinter.CTkFont(size=18), command=self.run_script)
        self.run_button.grid(row=7, column=0, padx=100, pady=60)

        # default values
        self.selection_menu.set("Select Script")

    # FUNCTIONS / COMMANDS

    def run_script(self):
        # get inputed values
        script_selection = self.selection_menu.get()
        row_amount = self.farming_rows.get()
        play_pause_keybind = self.play_pause_keybind.get()

        Hypixel.get_values(script_selection, row_amount, play_pause_keybind)


class Hypixel:
    def __init__(self) -> None:
        pass

    @staticmethod
    def sleep_with_pause(duration):
        """Sleeps for the specified duration, but checks for pause every 0.1 seconds."""
        end_time = time.time() + duration
        while time.time() < end_time:
            if keyboard.is_pressed(']'):
                return True
            time.sleep(0.1)
        return False

    @staticmethod
    def get_values(script, row_count, play_pause):

        script_selection = script
        row_count = int(row_count)
        play_pause_keybind = play_pause

        # debug
        print(script_selection)
        print(row_count)
        print(play_pause_keybind)

        if (script_selection == "Nether Wart"):
            Hypixel.nether_wart(row_count, play_pause)
        elif (script_selection == "Sugar Cane"):
            Hypixel.sugar_cane(row_count, play_pause)
        elif (script_selection == "Cactus"):
            Hypixel.cactus(row_count, play_pause)
        else:
            print("error")

    @staticmethod
    def nether_wart(row_count, play_pause_keybind):
        print("Nether wart script started")

        time.sleep(3)

        is_paused = True

        while True:
            if keyboard.is_pressed(play_pause_keybind):
                is_paused = not is_paused
                print("Paused" if is_paused else "Resumed")
                time.sleep(1)

            if not is_paused:
                x = 0
                pag.mouseDown()
                while x <= row_count - 2:
                    # Generate new number
                    time_to_walk_row = random.uniform(18.1, 18.15)

                    # Debug
                    print(time_to_walk_row)
                    print(x)

                    # Walk Right
                    keyboard.press('d')
                    if Hypixel.sleep_with_pause(time_to_walk_row):
                        keyboard.release('d')
                        break
                    keyboard.release('d')

                    # Walk Forward
                    keyboard.press('w')
                    if Hypixel.sleep_with_pause(0.97):
                        keyboard.release('w')
                        break
                    keyboard.release('w')

                    # Walk Left
                    keyboard.press('a')
                    if Hypixel.sleep_with_pause(time_to_walk_row):
                        keyboard.release('a')
                        break
                    keyboard.release('a')

                    if x < row_count - 2:
                        # Walk Forward
                        keyboard.press('w')
                        if Hypixel.sleep_with_pause(0.97):
                            keyboard.release('w')
                            break
                        keyboard.release('w')

                    x = x + 2
                pag.mouseUp()

                print("Farming complete.")
                sys.exit()

    @staticmethod
    def sugar_cane(row_count, play_pause_keybind):
        print("Sugar cane script started")

        time.sleep(3)

        is_paused = True

        while True:
            if keyboard.is_pressed(play_pause_keybind):
                is_paused = not is_paused
                print("Paused" if is_paused else "Resumed")
                time.sleep(1)

            if not is_paused:
                x = 0
                pag.mouseDown()
                while x <= row_count - 2:
                    # Generate new number
                    time_to_walk_row = random.uniform(9.525, 9.567)

                    # Debug
                    print(time_to_walk_row)
                    print(x)

                    # Walk Right
                    keyboard.press('d')
                    if Hypixel.sleep_with_pause(time_to_walk_row):
                        keyboard.release('d')
                        break
                    keyboard.release('d')

                    if x < row_count - 2:
                        # Walk Left
                        keyboard.press('s')
                        if Hypixel.sleep_with_pause(time_to_walk_row + 0.225):
                            keyboard.release('s')
                            break
                        keyboard.release('s')

                    x = x + 2
                pag.mouseUp()

                print("Farming complete.")
                sys.exit()

    @staticmethod
    def cactus(row_count, play_pause_keybind):
        print("Cactus script started")

        time.sleep(3)

        is_paused = True

        while True:
            if keyboard.is_pressed(play_pause_keybind):
                is_paused = not is_paused
                print("Paused" if is_paused else "Resumed")
                time.sleep(1)

            if not is_paused:
                x = 0
                pag.mouseDown()
                keyboard.press('s')
                while x <= row_count - 2:
                    # Generate new number
                    time_to_walk_row = random.uniform(15.01, 15.05)

                    # Debug
                    print(time_to_walk_row)
                    print(x)

                    if x > 0:
                        time.sleep(1.25)
                    # Walk Right
                    keyboard.press('d')
                    if Hypixel.sleep_with_pause(time_to_walk_row):
                        keyboard.release('d')
                        break
                    keyboard.release('d')

                    time.sleep(1.25)

                    if x < row_count - 2:
                        # Walk Left
                        keyboard.press('a')
                        if Hypixel.sleep_with_pause(time_to_walk_row):
                            keyboard.release('a')
                            break
                        keyboard.release('a')

                    x = x + 2
                pag.mouseUp()
                keyboard.release('s')

                print("Farming complete.")
                sys.exit()


if __name__ == "__main__":
    App = App()
    Hypixel = Hypixel()
    App.mainloop()
