import pyttsx3

class Voice:

    @staticmethod
    def speak(text):

        engine = pyttsx3.init()

        voices = engine.getProperty('voices')

        female_voice_found = False

        for voice in voices:
            if 'female' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                female_voice_found = True
                break
        
        if not female_voice_found:
            engine.setProperty('voice', voices[1].id)

        engine.setProperty('rate', 130)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()

    @staticmethod
    def prompt(text):
        print(text)
        Voice.speak(text)

# Voice.speak("Alisha : version-1.2 [ACTIVE]")