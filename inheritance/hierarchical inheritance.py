class Antagonist:
    def __init__(self, name):
        self.name = name

class MadaraUchiha (Antagonist):
    def speak(self):
        return f"{self.name} In this world, wherever there is light there are also shadows!"

class  Doflamingo(Antagonist):
    def speak(self):
        return f"{self.name} I'm not a god... I'm a human who became a demon! The weak don't get to decide anything, not even their own deaths!"

class Joker(Antagonist):
    def speak(self):
        return f"{self.name} I'm not a monster. I'm just ahead of the curve!"

if __name__ == "__main__":
    MadaraUchiha  = MadaraUchiha ("MadaraUchiha:")
    Doflamingo =  Doflamingo("Doflamingo:")
    Joker = Joker("Joker:")

    Antagonist = [MadaraUchiha , Doflamingo, Joker]

    for Antagonist in Antagonist:
        print(Antagonist.speak())


