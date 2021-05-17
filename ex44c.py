# Exercise 44c

class Person(object):

    def say(self, words):
        print(words)

class AnnoyingPerson(Person):

    # altered method
    def say(self, words):
        loud_words = words.upper() + '!!!'
        super(AnnoyingPerson, self).say(loud_words)

amy = Person()
bob = AnnoyingPerson()

amy.say('hello')
bob.say('hello')
