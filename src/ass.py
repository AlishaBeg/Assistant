import sys
import os
import time
import json
from datetime import datetime
from .io import Voice
from .theme import Theme
from .brain import Command

class Assist:

    def __init__(self, username):
        self.username = username

    @staticmethod
    def whoami():
        return self.username

    @staticmethod
    def loader(steps=32, delay=0.1, symbol="#", empty="_"):
        print()
        for i in range(steps + 1):
            percent = int((i / steps) * 100)
            bar = symbol * i + empty * (steps - i)
            sys.stdout.write("\r" + " " * 40)
            sys.stdout.write(f"\r [{bar}] {percent:>3}%")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    @staticmethod
    def log(action, log_file='data/status.log', level=0):

        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        STATUS = {
            0: "INFO",
            1: "WARNING",
            2: "ERROR"
        }
        line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {STATUS.get(level, "INFO"):<7} | {action}\n"
        
        with open(log_file, 'a', encoding="utf-8") as file:
            file.write(line)

    @staticmethod
    def choice(query):
        while True:
            Voice.speak(f"{query}")
            user_choice = input("\n- " + query + "? [Yes/No]: ").strip().lower()

            if user_choice.startswith("y"):
                return True
            elif user_choice.startswith("n"):
                return False
            else:
                print('Press Y if choice Yes OR N for No.')

    @staticmethod
    def welcome():
        Theme.welcome('Alisha (version-2.1) [ACTIVE] As Personal Assistant. What can i do for You?')
        Voice.speak(f"I am Alisha Your Personal Assistant &o What i can do for You?")
        Command.shell()