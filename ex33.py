# ex 33

## Animal is-a object
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has a init
        self.name = name

## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## has a
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## has a
        self.name = name
        ## person has a pet
        self.pet = None

## Employee is=a person
class Employee(Person):

    def __init__(self, name, salary):
        ## has a
        super(Employee, self).__init__(name)
        ## has a
        self.salary = salary

## fish is a object
class Fish(object):
    pass

# koi is-a fish
class Koi(Fish):
    pass

## halibut is a fish
class Halibut(Fish):
    pass

#rover is a dog
rover = Dog("Rover")

# satan is a cat
satan = Cat("Satan")

# mary is a person
mary = Person("Mary")

## mary has a pet named satan / pet is-a satan
mary.pet = satan

# frank is an employee and has a salary of 120000
frank = Employee("Frank", 120000)

# frank has a pet named rover
frank.pet = rover

#flipper is a fish
flipper = Fish()

# kyle is a koi
kyle = Koi()

# harry is a halibut
harry = Halibut()
