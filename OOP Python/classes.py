class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hello I am", self.name, "and I am", self.age, "years old.")

    def talk(self):
        print("Bark")

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("Meow")


cat = Cat("Fred", 30, "blue")
cat.speak()
cat.talk()

dog = Dog("Jim", 40)
dog.speak()
dog.talk()