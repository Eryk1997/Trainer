from Connect.Connect import mydb
import bcrypt


class Trainer:
    def __init__(self, fullName, email, password, passwordConfirm):
        self.fullName = fullName
        self.email = email
        self.password = password
        self.passwordConfirm = passwordConfirm

    # getters
    def getFullName(self):
        return self.fullName

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password

    # setters
    def setFullName(self, fulName):
        self.fullName = fulName

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password

    def hash_password(self):
        pom = bytes(self.password, 'utf-8')
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(pom, salt)


    def verify_password(self, passwordVerify):
        print(self.password)
        print(passwordVerify)
        if bcrypt.checkpw(passwordVerify, self.password):
            print("good")
        else:
            print("bad")

    def addTrainerDatabase(self):
        mycursor = mydb.cursor()

        sql = "INSERT INTO `Trainers` VALUES (NULL, %s, %s, %s);"
        mycursor.execute(sql, (self.getFullName(), self.getEmail(), self.getPassword()))

        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
