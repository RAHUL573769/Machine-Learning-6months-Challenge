class Human:
    def __init__(self, legs):
        self.num_heart = 1
        self.legs = legs

    def eat(self, name, num_heart):
        self.name = name
        self.num_heart = num_heart
        print(f'I can eat {self.name}')


class Male:
    def __init__(self, name):
        self.nose = 3
        self.name = name

    def flirt(self):
        self.nose = 1
        print(f'I can and have {self.nose} nose')


class Boy(Human, Male):
    def __init__(self, name, legs=2):
        Male.__init__(self, name)
        Human.__init__(self, legs)


boy1 = Boy("Rahul")
print('18', boy1.name, boy1.legs)

boy1.legs = 1  # change legs
print("Legs", boy1.legs)

print('18', boy1.num_heart)

boy1.eat("Mango", 1)
boy1.flirt()


class Human1:
    def eat(self):
        print("I can eat")
class Male(Human1):
