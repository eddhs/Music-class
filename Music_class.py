class Musician(object):
    def __init__(self,sounds):
        self.sounds =sounds
    def solo(self,length):
        for x in range(length):
            print(self.sounds[x % len(self.sounds)], end=" ")
        print()

class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Thwomp", "Ting", "Tick"])
    def count(self):
        print("Aaaaand 1, 2, 3, 4")
    def combust(self):
        print("KABOOOOM")

class Band(Musician):
    def __init__(self):
        super().__init__(["Thwomp", "Ting", "Tick"])
    def  start_playing(self):
        if __name__=="__main__":
            gabe.count()
            nigel.solo(6)
            mark.solo(4)
            gabe.solo(5)
 
                
        
nigel = Guitarist()
mark = Bassist()
gabe = Drummer()
Pythons = Band()

Pythons.start_playing()

