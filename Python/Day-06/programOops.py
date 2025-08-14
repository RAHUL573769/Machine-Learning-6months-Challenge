class Circle:
    pie=3.14
    def __init__(self,radius):
        self.radius=radius
    def area(self,value):
        areaValue = (Circle.pie * self.radius ** 2)
        print(value)
        return  areaValue


areaOfCircle=Circle(2)
print(areaOfCircle.area("hi"))



