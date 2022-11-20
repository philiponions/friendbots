import random
from time import sleep
import pyttsx3
import threading

class Bot:
    def __init__(self, voice_type):
        self.engine = pyttsx3.init()    
        self.engine.setProperty('voice', voice_type)
        self.voice_type = voice_type
    
    def talk(self, dialogue):

        threading.Thread(
            target=self.run_pyttsx3(dialogue), args=(None), daemon=True
        ).start()
        
    
    def run_pyttsx3(self, text):
        engine = pyttsx3.init() 
        engine.setProperty('voice', self.voice_type)
        engine.say(text)
        engine.runAndWait()



class Evanne(Bot):
    def __init__(self):
        super().__init__('com.apple.speech.synthesis.voice.nicky')
        self.dialogue = "OMG GUYS LET MEEE TELL YOU..."

    def say_something(self):
        sleep(1)
        
        # super().talk(self.dialogue)
        # print("Evanne says: " + self.dialogue)      
        return self.dialogue

class Evelyn(Bot):
    def __init__(self):
        super().__init__('com.apple.speech.synthesis.voice.samantha')
        self.dialogue = "Hullo!"
    def say_something(self, message):
        sleep(1)
        dialogue = self.dialogue
        index = random.randint(1,3)
        
        if (index == 3):
            dialogue = "o"

        # print("Evelyn says: " + self.dialogue)      
        # super().talk(self.dialogue)
        return self.dialogue


class Ilti(Bot):
    def __init__(self):
        super().__init__('com.apple.speech.synthesis.voice.karen')
        self.dialogues = ["Hey guiseeee (peer support voice)", "DEADASS (skull emoji)", "Sorry i have a party (crying emoji)"]
    def say_something(self):
        thinking_time = random.randint(1, 5)
        sleep(thinking_time)
        index = random.randint(0, len(self.dialogues) - 1)
        
        # print("Ilti says: " + self.dialogues[index])   
        # super().talk(self.dialogues[index])
        return self.dialogues[index]

class Kiara(Bot):
    def __init__(self):
        super().__init__('com.apple.speech.synthesis.voice.melina')
        self.dialogue = "i love inwoo"
    def say_something(self):
        sleep(1)

        # print("Kiara says: " + self.dialogue)   
        # super().talk(self.dialogue)
        return self.dialogue

class Huey(Bot):
    def __init__(self):
        super().__init__('com.apple.speech.synthesis.voice.daniel')
        self.dialogues = ["I'm driving", "I want a thinkpad", "linux all the way", "huhhhhh i need a new gpu", "HEY GUYS I APPLIED TO AN INTERNSHIP", "IMMA POWER USER", "you got any protein??", "wanna work out???"]
    
    # TODO: Not scalable, refactor soon. Have sigma super class and have Huey and Alex inherit
    def say_something(self):
        thinking_time = random.randint(1, 5)
        sleep(thinking_time)
        index = random.randint(0, len(self.dialogues) - 1)

        # print("Huey says: " + self.dialogues[index])   
        # super().talk(self.dialogues[index])
        return self.dialogues[index]


class Alex(Bot):
    def __init__(self):
        super().__init__('com.apple.speech.synthesis.voice.alex')
        self.dialogues = ["HEY GOOGLE LIGHTS ON", "I NEED BIKE PARTS", "LETS GO SKIING", "RTX 3080", "ENGG","MY CLASSES SUCK, I HATE ENGG", "BETA SIGMA MALE GRIND SET", "GET THEM GAINS", "'minimalist setup'"]
    def say_something(self, message):
        thinking_time = random.randint(1, 5)
        sleep(thinking_time)
        index = random.randint(0, len(self.dialogues) - 1)

        # print("Alex says: " + self.dialogues[index])   
        # super().talk(self.dialogues[index])
        return self.dialogues[index]

def main():    

    kiara = Kiara()
    alex = Alex()
    evanne = Evanne()
    huey = Huey()
    ilti = Ilti()
    evelyn = Evelyn()

    while True:
        probability = random.randint(1,3)
        if probability == 3:
            evanne_dialogue = evanne.say_something()
            print("E-vanne says: " + evanne_dialogue)            
            evanne.talk(evanne_dialogue)

            huey_dialogue = huey.say_something()
            print("Huey says: " + huey_dialogue) 
            huey.talk(huey_dialogue)           

        kiara_dialogue = kiara.say_something()
        print("Kiara says: " + kiara_dialogue) 
        kiara.talk(kiara_dialogue)                  

        alex_dialogue = alex.say_something(kiara_dialogue)
        print("Alex says: " + alex_dialogue)        
        alex.talk(alex_dialogue)           

        evelyn_dialogue = evelyn.say_something(alex_dialogue)
        print("Evelyn says: " + evelyn_dialogue)        
        evelyn.talk(evelyn_dialogue)           

        huey_dialogue = huey.say_something()
        print("Huey says: " + huey_dialogue)   
        huey.talk(huey_dialogue)                

        ilti_dialogue = ilti.say_something()
        print("Ilti says: " + ilti_dialogue)
        ilti.talk(ilti_dialogue)           


main()
