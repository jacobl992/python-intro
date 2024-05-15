class Point:
    def move(self):
        print("move")


    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
#point1 and point2 are both seperate instances of the Point class
# They can draw on the same methods, but have different values

