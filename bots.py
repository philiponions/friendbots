import random
from time import sleep

class Evanne:
    def __init__(self):
        self.dialogue = "OMG GUYS LET MEEE TELL YOU..."
    def say_something(self):
        sleep(1)
        return self.dialogue

class Evelyn:
    def __init__(self):
        self.dialogue = "Hullo!"
    def say_something(self, message):
        sleep(1)
        dialogue = self.dialogue
        index = random.randint(1,3)
        
        if (index == 3):
            dialogue = "o"

        return self.dialogue


class Ilti:
    def __init__(self):
        self.dialogues = ["Hey guiseeee (peer support voice)", "DEADASS (skull emoji)", "Sorry i have a party (crying emoji)"]
    def say_something(self):
        thinking_time = random.randint(1, 5)
        sleep(thinking_time)
        index = random.randint(0, len(self.dialogues) - 1)
        return self.dialogues[index]

class Kiara:
    def __init__(self):
        self.dialogue = "i love inwoo"
    def say_something(self):
        sleep(1)
        return self.dialogue

class Huey:
    def __init__(self):
        self.dialogues = ["I'm driving", "I want a thinkpad", "linux all the way", "huhhhhh i need a new gpu", "HEY GUYS I APPLIED TO AN INTERNSHIP", "IMMA POWER USER", "you got any protein??", "wanna work out???"]
    
    # TODO: Not scalable, refactor soon. Have sigma super class and have Huey and Alex inherit
    def say_something(self):
        thinking_time = random.randint(1, 5)
        sleep(thinking_time)
        index = random.randint(0, len(self.dialogues) - 1)
        return self.dialogues[index]


class Alex:
    def __init__(self):
        self.dialogues = ["HEY GOOGLE LIGHTS ON", "I NEED BIKE PARTS", "LETS GO SKIING", "RTX 3080", "ENGG","MY CLASSES SUCK, I HATE ENGG", "BETA SIGMA MALE GRIND SET", "GET THEM GAINS", "'minimalist setup'"]
    def say_something(self, message):
        thinking_time = random.randint(1, 5)
        sleep(thinking_time)
        index = random.randint(0, len(self.dialogues) - 1)
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
        
            huey_dialogue = huey.say_something()
            print("Huey says: " + huey_dialogue)
        
        kiara_dialogue = kiara.say_something()
        print("Kiara says: " + kiara_dialogue)
        
        alex_dialogue = alex.say_something(kiara_dialogue)
        print("Alex says: " + alex_dialogue)
     
        evelyn_dialogue = evelyn.say_something(alex_dialogue)
        print("Evelyn says: " + evelyn_dialogue)

        huey_dialogue = huey.say_something()
        print("Huey says: " + huey_dialogue)

        ilti_dialogue = ilti.say_something()
        print("Ilti says: " + ilti_dialogue)

main()
