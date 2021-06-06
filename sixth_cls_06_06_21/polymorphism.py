class Animal:

    def __init__(self, a, s):
        self.a = a
        self.s = s

    def shout(self):
        print(self.a, self.s)


class Dog(Animal):
    pass


class Cat(Animal):
    pass


animal = Animal("Dog", "Bark")

d = Dog(animal.a, animal.s)
print(d.shout())
animal2 = Animal("Cat", "Mew")
c = Cat(animal2.a, animal2.s)
print(c.shout())



