from TrainerClass.Trainer import Trainer

fullName = input("Enter your fullName: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
passwordConfirm = input("Enter your password confirm: ")

if fullName != '' and email != '' and password != '' and (password == passwordConfirm):
    newTrainer = Trainer(fullName, email, password, passwordConfirm)
    newTrainer.hash_password()
    newTrainer.addTrainerDatabase()
else:
    print("bad value")
