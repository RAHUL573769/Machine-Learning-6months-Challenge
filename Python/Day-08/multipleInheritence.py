class Human:
    def eat(self):
        print("I can eat")
class Male:
    def flirt(self):
        print("I can Flirt")
class Boy(Human,Male):
    pass

boy1=Boy()
print(boy1.eat())