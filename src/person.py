import sys
import time

from .io import Voice

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

    
    def gender(self):
        if self.choice("Are you male?"):
            print("\n- Ich hoffe, du entpuppst dich nicht als Hund")  # hope you don't turn out to be a dog
            self.hasMale = True
        else:
            print("\n- Ich hoffe, du entpuppst dich nicht als Schlampe")  # hope you don't turn out to be a bitch

        time.sleep(1)
        print("\nPlease forgive me, I was just trying to get you!")

    def hisShe(self):
        if self.choice("Is that a girl?"):
            self.isShe = True

            if self.name.upper() == self.developer:
                sex = 1
            else:
                if (self.hasMale and self.isShe) or (not self.hasMale and not self.isShe):
                    sex = 1
                elif not self.hasMale and self.isShe:
                    sex = 2
                elif self.hasMale and not self.isShe:
                    sex = 3
            self.whoshe()
        else:
            print("\n- But I am a Girl.")
            time.sleep(2)
            self.purposeal()

    def whoshe(self):
        if self.his_name() == 'YOU':
            if self.name == self.developer:
                print("\n- Ich bin froh")  # I am feeling glad
            elif self.name == 'DEVIL':
                print("\n- Nachdem Sie das gehört haben, werden Sie nass")  # You will get wet after hearing this
            else:
                print("\n- Good to know!")
            self.ami()
        else:
            print(f"\n- {self.friend}, Nice")
            time.sleep(1)
            if self.choice("Do you like that?"):
                self.likeShe = True
                if self.choice("Have you had sex?"):
                    self.isVirgin = False
                    if self.name.upper() == self.developer:
                        self.choice("\nHast du dich verliebt?")  # So have you fallen in love?
                    elif self.name.upper() == 'DEVIL':
                        print("\n- Das heißt, sie ist deine Hure.")  # That means she's your whore.
                    else:
                        print("\n- Das bedeutet, dass sie deine Geliebte ist.")  # That means she's your lover.
                    time.sleep(1)
            else:
                self.choice("So have any crush?")
            self.purposeal()

    def his_name(self):
        while True:
            self.friend = input("\nWhat is his name? ").strip()
            if len(self.friend) != 0:
                return self.friend.upper()
            print("Please enter a valid name.")

    def purposeal(self):
        if self.choice("Let's be friends?"):
            print("\n- The pleasure was all mine. :)")
            time.sleep(1)
            self.ami()
        else:
            print("\n- I think you have a chance.")
            time.sleep(1)
            if self.choice("I want to be your friend?"):
                self.ami()
            else:
                print("\n- Das hat mir das Herz gebrochen")  # This broke my heart
        self.bye()

    def bye(self):
        if self.choice("Hope you enjoy?"):
            if self.choice("Please, let me go now?"):
                if self.name.upper() == self.developer:
                    print("\n- Liebe dich")  # Love you
                elif self.name.upper() == 'DEVIL':
                    print("\n- Nimm mein nächstes Mal")  # Take mine next time
                else:
                    print("\n- See you later")
                return
            else:
                print("\n- Bitte")  # Please
        else:
            if self.hasDeveloper:
                print("\n- Verzeihen Sie mir")  # Forgive me
            else:
                print("\n- Stell dich zurück")  # Put yourself behind

    def friend(self):
        self.isDeveloper(self.enter_name())
        input("Press Enter to continue: ")
        print("\nOK\n")
        if self.choice("Do you have any friends?"):
            self.hisShe()
        else:
            self.purposeal()