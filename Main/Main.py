from TrainerClass.Trainer import Trainer

trainer = Trainer("Eryk Janocha", "erykmati@o2.pl", "xx", "xx")
print(trainer.getEmail())
trainer.setEmail("eryk.janocha@interia.pl")
print(trainer.getEmail())
