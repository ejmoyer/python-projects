# Ex 44A

class Dog(object):

    #implicit method
    def bark(self):
        print('woof!')

class Poodle(Dog):
    pass

fido = Dog()
spot = Poodle()

fido.bark()
spot.bark()
