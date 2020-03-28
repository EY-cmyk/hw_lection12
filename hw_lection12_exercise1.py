class Animal():
    def __init__(self,talk):
        self.talk = talk


class Dog(Animal):
    def talk(self):
        self.name = Dog
        print('WOOf WOOOOf')


class Cat(Animal):
    def talk(self):
        self.name = Cat
        print("MEOWWW MWOOOWWW")

andy = Dog()
print(andy.talk())

catty = Cat()
print(catty.talk())
