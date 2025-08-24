import os
import sys
import time
import json
import bcrypt
import getpass
from datetime import datetime
from .io import Voice
from .ass import Assist
from .theme import Theme

class Primary:

    @staticmethod
    def enter_name():
        while True:
            Voice.speak('Please enter you username')
            name = input("\n ~ enter username : ").strip()
            if len(name) != 0:
                return name
            print("Please enter a your name.")

    @staticmethod
    def isSecure(username):
        try:
            with open('data/admin.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                admin_list = data.get('admin', [])
        except FileNotFoundError:
            Voice.prompt('\nAdmin data file not found. Exiting.\n')
            sys.exit(1)
        except json.JSONDecodeError:
            Voice.prompt('\nAdmin data file is corrupted. Exiting.\n')
            sys.exit(1)

        for admin in admin_list:
            if admin.get('username') == username:
                Voice.speak(f"Access to confirm your password, {username}")
                password = getpass.getpass(" ~ enter password : ")

                stored_hash = admin.get('password')
                if stored_hash and bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
                    return True
                else:
                    return False
        return False

    @staticmethod
    def scan(dataList):
        missed = []
        for f in dataList:
            if not os.path.exists(f):
                missed.append(f)
        if not missed:
            return True

        print("\n[ WARNING : FILE NOT FOUND ]\n")
        for file_path in missed:
            print("\t -", file_path)
        Voice.speak('A required file is missing. The system might be corrupted.')
        sys.exit(1)


class Secondary:

    @staticmethod
    def active():
        Voice.prompt('\n Secondary protocol is (active)')

        Assist.log('secondary protocol is active')

        if Assist.choice('Did you open me by mistake'):
            Voice.prompt('\n { Please avoid opening without permission }')
            Assist.log('open with mistake')
            sys.exit(1)

        Voice.prompt("\n This is you final chance with time limit &o")

        if Assist.choice('You open me by mistake'):
            Voice.prompt('\n { Access is terminated } DONNOT DARE AGAIN (ilii)')
            Assist.log('access is terminated')
            sys.exit(1)

        username = Primary.enter_name()

        if Primary.isSecure(username):
            Assist.log('access is granted')
            Access.GRANTED()
        else:
            Assist.log('access is locked')
            Secondary.punish()

    @classmethod
    def punish(cls):
        print()
        print("="*50)
        Voice.prompt("\n - Primary Protocol is   \t (failed)")
        Voice.prompt("\n - Secondary Protocol is \t (failed) \n")
        print("-"*50)
        Voice.prompt('\n You attempt invalid access me \t System is (locked)')
        if Assist.choice("did you save us"):
            unlock = input(" HOW? : ")
        Theme.fuck()
        sys.exit(1)

class Access:

    __PROJECT = [
        "data/status.log",
        "data/admin.json",
        "src/network.py",
        "src/system.py",
        "src/theme.py",
        "src/file.py",
        "src/ass.py",
        "src/io.py",
        "app.py",
    ]

    @classmethod
    def GRANTED(cls):
        print("\n\t[ ACCESS IS GRANTED ]\n")
        Voice.speak("Access is granted")
        Assist.welcome()

    @classmethod
    def DENIED(cls):
        print("\n\t[ ACCESS IS DENIED ]\n")
        Voice.speak("Access is denied")
        Secondary.active()

    @staticmethod
    def secure():

        Voice.prompt(" Alisha : version-1.2 [LOADING]")
        
        Assist.loader()

        Assist.log('primary protocol is active')

        if Primary.scan(Access.__PROJECT):
            Voice.prompt("\n Primary protocol is (active)")

        user = Primary.enter_name()

        if Primary.isSecure(user):
            Assist.log('access id granted')
            Access.GRANTED()
        else:
            Assist.log('access is denied')
            Access.DENIED()
