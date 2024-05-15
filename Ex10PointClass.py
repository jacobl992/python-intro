class Point:
    def __init__(self, x, y):
        #magic method constructor
        self.x = x
        self.y = y
        #setting the x or y attribute to the x or y argument passed to this function
        #the correct syntax for Python is to use two blank lines after functions/methods


    def move(self):
        print("move")


    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.x = 10
print(point1.x)
point1.x = 11
print(point1.x)
point1.draw()

point2 = Point(12, 50)
point2.x = 1
#point1 and point2 are both seperate instances of the Point class
# They can draw on the same methods, but have different values

#another class example

class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f'Hi, I am {self.name}')


john = Person('John Smith')
john.talk()

bob = Person('Bob Smith')
bob.talk()
