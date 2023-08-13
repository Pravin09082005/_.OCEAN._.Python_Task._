class Father:
    def __init__(self,aName):
        self.Father= aName

class Mother:
    def __init__(self,dName):
        self.Mother= dName

class son(Father,Mother):
    def __init__(self,aName,dName):
        Father.__init__(self,aName)
        Mother.__init__(self,dName)


obj= son("Bardock","Gine")
print("Son:Goku")
print("Father:",obj.Father)
print("Mother:",obj.Mother)
