import os
import time
import keyboard
from termcolor import colored
from colorant import Colorant

os.system('color')
os.system('title Colorant')

TOGGLE_KEY = 'F1'
FOV = 50
CENTER_X, CENTER_Y = 1920 // 2, 1080 // 2

class Main:
    def __init__(self):
        self.colorant = Colorant(CENTER_X - FOV // 2, CENTER_Y - FOV // 2, FOV)
        self.status = 'Disabled'

    def print(self):
        print(colored('''
                         ▄████▄   ▒█████   ██▓     ▒█████   ██▀███   ▄▄▄       ███▄    █ ▄▄▄█████▓
                        ▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▒██▒  ██▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                        ▒▓█    ▄ ▒██░  ██▒▒██░    ▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                        ▒▓▓▄ ▄██▒▒██   ██░▒██░    ▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                        ▒ ▓███▀ ░░ ████▓▒░░██████▒░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                        ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                          ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                        ░        ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒    ░░   ░   ░   ▒      ░   ░ ░   ░      
                        ░ ░          ░ ░      ░  ░    ░ ░     ░           ░  ░         ░          
                        ░                                                                         
                                                  COLOR AIMBOT - v1.0''', 'magenta'))
        print()
        print(colored('[Info]', 'green'), colored('Set enemies to', 'white'), colored('Purple', 'magenta'))
        print(colored('[Info]', 'green'), colored(f'Press {TOGGLE_KEY} to toggle ON/OFF', 'white'))
        print(colored('[Info]', 'green'), colored('Default settings are', 'white'),
              colored('RightMB', 'magenta'), colored('= Aimbot,', 'white'),
              colored('LeftAlt', 'magenta'), colored('= Triggerbot', 'white'))
        print(colored('[Info]', 'green'), colored('GitHub Repo:', 'white'),
              '\033[35;4mhttps://github.com/hafyzwithawhy/Colorant\033[0m')
        print(colored('[Info]', 'green'), colored('Made By', 'white'), colored('Hafez#6866', 'magenta'))

    def toggle_aimbot(self):
        if keyboard.is_pressed(TOGGLE_KEY):
            self.colorant.toggle()
            self.status = 'Enabled ' if self.colorant.toggled else 'Disabled'

    def run(self):
        try:
            self.print()
            while True:
                self.toggle_aimbot()
                print(f'\r{colored("[Status]", "green")} {colored(self.status, "white")}', end='')
                time.sleep(0.01)
        except (KeyboardInterrupt, SystemExit):
            print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
        finally:
            self.colorant.close()

def main():
    aimbot = Main()
    aimbot.run()

if __name__ == '__main__':
    main()
