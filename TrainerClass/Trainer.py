class Trainer:
    def __init__(self, fullName, email, password, passwordConfirm):
        self.fullName = fullName
        self.email = email
        self.password = password
        self.passwordConfirm = passwordConfirm

    # getters
    def getFullName(self): return self.fullName

    def getEmail(self): return self.email

    def getPassword(self): return self.password

    # setters
    def setFullName(self, fulName): self.fullName = fulName

    def setEmail(self, email): self.email = email

    def setPassword(self, password): self.password = password
