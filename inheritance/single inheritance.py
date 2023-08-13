class Cars:
    def __init__(self, aName):
        self.Cars=aName

class Supra(Cars):
    def __init__(self, aName):
        self.supra=aName

obj=Cars("Supra")
print(obj.Cars)

