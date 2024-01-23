class car(object):
    def __init__(self, make, model, year, condition="New", kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms." % (self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s." % (self.make, self.model, self.year))

car1 = car("Ford", "Fusion", 2024)
car1.display(True)