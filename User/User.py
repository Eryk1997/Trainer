class User:
    def __init__(self, fullName, email, height, weight, age):
        self.fullName = fullName
        self.email = email
        self.height = height
        self.weight = weight
        self.age = age

    # getters
    def getFullName(self): return self.fullName

    def getEmail(self): return self.email

    def getHeight(self): return self.height

    def getWeight(self): return self.weight

    def getAge(self): return self.age

    # setters
    def setFullName(self, fullName): self.fullName = fullName

    def setEmail(self, email): self.email = email

    def setHeight(self, height): self.height = height

    def setWeight(self, weight): self.weight = weight

    def setAge(self, age): self.age = age
