class Human:
    def __init__(self):
        self.nam="Rahul"
    def eat(self):

        print("eat")
    def work(self):
        print("Work")
class Male(Human):
    def flirt(self):
        print(f' {self.nam} can Flirt')

    def work(self):
        super().work()
        print("I can code")

male1=Male()
print(male1.eat())
print(male1.flirt())
print(male1.work())