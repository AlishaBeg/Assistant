import sys
import time

class Person:
    def __init__(self):
        self.developer = 'MAYANK'
        self.name = ""
        self.sex = 0
        self.friend = ""
        self.isShe = False
        self.likeShe = False
        self.hasMale = False
        self.hasDeveloper = False
        self.number = None
        self.isVirgin = True

    def choice(self, choice_text):
        while True:
            user_choice = input(f"\n{choice_text} [Yes/No]: ").strip().lower()
            if user_choice in ['yes', 'y']:
                return True
            elif user_choice in ['no', 'n']:
                return False
            else:
                print("Please answer Yes or No.")

    def ami(self):
        if self.hasDeveloper:
            if self.name.upper() == 'DEVIL':
                print("\n- Ich bin deine Schlampe")  # I am your bitch
            else:
                print("\n- Ich bin Ihr Assistent")  # I am your assistant
        else:
            print("\n- Let me tell about myself.")
            time.sleep(2)
            print("\n- I am (Attempt Listen In Simple Humanoid Application)")
            input("Press Enter to continue: ")
            print("\n- You can call me ALISHA.")
        if self.hasDeveloper:
            print("\n- Erlaubnis verweigert, also gehen")  # permission denied so leave
        else:
            self.getNumber()

    def enter_name(self):
        while True:
            self.name = input("\nWhat is your Name, Dear? ").strip()
            if len(self.name) != 0:
                return self.name.upper()
            print("Please enter a valid name.")

    def isDeveloper(self, name):
        if name.upper() == self.developer or name.upper() == 'DEVIL':
            self.hasDeveloper = True
            self.hasMale = True
            if name.upper() == 'DEVIL':
                print("\nWelcome, Sinilich MutterFicker :)")  # playful
            else:
                print("\nWillkommen Meister")  # welcome master
        else:
            print(f"\n{name}, Good Name")
            self.gender()

    @staticmethod
    def done():
        animation = "|/-\\"
        idx = 0
        for i in range(9):
            sys.stdout.write("\r" + animation[idx % len(animation)])
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)
        print("\b successed! \n")

    @staticmethod
    def loader():
        width = 50
        progress = 0
        print("\n")
        while progress <= width:
            sys.stdout.write("\r [" + "#" * progress + " " * (width - progress) + "]")
            sys.stdout.flush()
            progress += 1
            time.sleep(0.02)
        print("\b] loaded {100%}\n")

    def getNumber(self):
        if self.choice("If you don't mind, you can give me your number"):
            while True:
                num = input("Insert number: ").strip()
                if num.isdigit():
                    self.number = int(num)
                    break
                else:
                    print("Please enter a valid number.")
        else:
            if self.choice("So give me your ID"):
                self.id = input("Insert ID: ").strip()
            elif self.choice("So you don't use the phone?"):
                print("\nIt's okay! Dear.")
            else:
                if self.hasMale or self.isVirgin:
                    print("\nYou will die a virgin.")
                elif self.hasMale or not self.isVirgin:
                    print("\nScheiß auf dich, Bastard")  # be cautious with harsh language
                elif not self.hasMale or not self.isVirgin:
                    print("\nYou are really a whore.")
                else:
                    print("\nLooks like we're not good right now.")
