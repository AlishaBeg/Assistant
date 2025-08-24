import os
import sys
from datetime import datetime
from .io import Voice
from .theme import Theme
from .system import System
from .network import Network

class Command:

    @classmethod
    def ghost(cls, command):

        # No command 
        if not command:
            return
        
        # return
        if command.lower() in ("fuck", "bitch", "slut", "whore"):
            # "Если я скажу, что сниму трусики или бюстгальтер перед вами, спрошу, как пожелаете, Мастер."
            Voice.speak("Yesli ya skazhu, chto snimu trusiki ili byustgalter pered vami, sproshu, kak pozhelaete, Master.") 

        args = command.strip().split(maxsplit=2)
        command = args[0].upper() if args else ""

        # Exit
        if command.upper() in ("EXIT", "QUIT", "CLOSE"):
            Voice.prompt("Alisha (version-2.1) is [CLOSED]")
            sys.exit(0)

        # Is online
        elif command.upper() in ("NETWORK", "NET") and args[1].upper() == "STATUS":
            if Network.isOnline():
                Voice.prompt("\n system is (online) \n")
            else:
                Voice.prompt("\n system is (offline) \n")

        # Machine address
        elif command.upper() in ("MAC", "MACHINE") and args[1].upper() == "ADDRESS":
            Voice.prompt(f"{Network.mac()}")

        # Hostname
        elif command.upper() == "HOSTNAME":
            Voice.prompt(Network.hostname())

        # IP ADDRESS
        elif command.upper() == "IP":
            if args[1] == "PUTLIC":
                Voice.prompt(Network.public_ip())
            else:
                Voice.prompt(Network.ip())

        # STATUS
        elif command.upper() == "STATUS":
            System.information()
        
        # Time
        elif command.upper() == "TIME":
            hour = datetime.now().hour
            greet = "Morning" if hour < 12 else "Afternoon" if hour < 18 else "Evening" if hour < 24 else "Night"
            Voice.prompt(f"{greet} — {datetime.now().strftime('%A, %Y-%m-%d %H:%M:%S')}")

        # Who
        elif command.upper() == "WHO":
            Theme.who()
            Voice.speak("I am Alisha, your personal assistant.")

        # Whoami
        elif command.upper() == "WHOAMI":
            Voice.prompt("You are Mayank.")

        # Current directory
        elif command.upper() == "PWD":
            File.pwd()

        # List directory
        elif command.upper() in ("LS", "LIST"):
            File.ls(args[1])

        # Read file
        elif command.upper() in ("READ", "PRINT"):
            if len(args) < 2:
                Voice.prompt("Required file location")
                return
            File.read(args[1])

        # Write file
        elif command.upper() == "WRITE":
            if len(args) < 3:
                Voice.prompt("Required file location and data")
                return
            File.write(args[1], args[2])

        # Append file
        elif command.upper() == "APPEND":
            if len(args) < 3:
                Voice.prompt("Required file location and data")
                return
            File.append(args[1], args[2])

        # Delete file
        elif command.upper() == "DELETE":
            if len(args) < 2:
                Voice.prompt("Required file location")
                return
            File.delete(args[1])

        # Make directory
        elif command.upper() == "MKDIR":
            if len(args) < 2:
                Voice.prompt("Required directory name")
                return
            File.mkdir(args[1])

        # Remove directory
        elif command.upper() == "RMDIR":
            if len(args) < 2:
                Voice.prompt("Required directory name")
                return
            File.rmdir(args[1])

        # Rename file & directory
        elif command.upper() == "RENAME":
            if len(args) < 2:
                Voice.prompt("Required (old OR new) file name")
                return
            File.rename(args[1], args[2])

        # Rename file & directory
        elif command.upper() == "RENAME":
            if len(args) < 2:
                Voice.prompt("Required (old OR new) file name")
                return
            File.rename(args[1], args[2])

        # Move file & directory
        elif command.upper() == "MOVE":
            if len(args) < 2:
                Voice.prompt("Required (old OR new) location")
                return
            File.move(args[1], args[2])

        # Copy file & directory
        elif command.upper() == "COPY":
            if len(args) < 2:
                Voice.prompt("Required (old OR new) location")
                return
            File.copy(args[1], args[2])

        # touch file
        elif command.upper() == "TOUCH":
            if len(args) < 1:
                Voice.prompt("Required file name")
                return
            File.touch(args[1])

        # detail file & folder
        elif command.upper() == "DETAIL":
            if len(args) < 1:
                Voice.prompt("Required file & folder")
                return
            File.detail(args[1])

        # Unknown command
        else:
            Voice.speak(f"{command} command is terminated")

    @staticmethod
    def shell():
        while True:
            inThe = input(f"[{"ONLINE" if Network.isOnline else "OFFLINE"}] ~ ")
            Command.ghost(inThe)
