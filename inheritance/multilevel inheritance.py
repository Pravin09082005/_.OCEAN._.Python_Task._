class Animals:
    def __init__(self, aName):
        self.animals=aName

class Doggy(Animals):
    def __init__(self, dName):
        self.doggy=dName

class Puppy(Doggy):
    def __init__(self, aName, dName):
        Animals.__init__(self,aName)
        Doggy.__init__(self,dName)


obj = Puppy("Dog", "Lab")
        
        
print(obj.animals)
print(obj.doggy)