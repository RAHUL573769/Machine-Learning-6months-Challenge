class Instructor:
    followers=0
    def __init__(self,name,address):
        self.name=name
        self.address=address

        print("Creating a new Object")
    def display_actions(self,actions):
        print("Hi", actions)
    def update_followers(self,followers):
        self.followers=self.followers+1

        print(f'My name is {self.name} address is {self.address} Followers:{self.followers}')





instructor=Instructor("Rahul",'patuli')
print(instructor.update_followers(2))