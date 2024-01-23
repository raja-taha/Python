class Dog(object):
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _ in range(n):
            print('bark')


dog1 = Dog("Dog1")
dog2 = Dog("Dog2")

print(Dog.num_dogs())
print(dog1.bark(5))