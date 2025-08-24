import time
from personality import Person

class Hallo(Person):

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
