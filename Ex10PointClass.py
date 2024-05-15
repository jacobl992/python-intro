class Point:
    def __init__(self, x, y):
        #magic method constructor
        self.x = x
        self.y = y
        #setting the x or y attribute to the x or y argument passed to this function


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

