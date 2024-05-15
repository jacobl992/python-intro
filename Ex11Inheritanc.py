class Mammal:
    def walk(self):
        print('walk')


class Dog(Mammal):
    #include parent class in arguments for child class
    def wag(self):
        print('wag')


class Cat(Mammal):
    pass
    #pass allows creation of an empty class

dog1 = Dog()
dog1.walk()