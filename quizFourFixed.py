# Quiz: Week 04

# Instructions
# Edit this file and upload it to the quiz on the portal.
# Follow the directions of all comments and run the file
# to make sure there are no errors.

# 1
# Show a quality example of *implicit inheritance*
class BaseScene(object):

    def set_scene_name(self, scene_name):
        self.scene_name = scene_name

    def set_description(self, description):
        self.description = description

class SpaceScene(BaseScene):

    def tell_description(self):
        print(f"Current Scene:{self.scene_name}")
        print(self.description)

newScene = SpaceScene()
newScene.set_scene_name('Space')
newScene.set_description('A black void with stars and planets')

newScene.tell_description()

# 2
# Show a quality example of *implicit composition*
class Phrase(object):

    def say(self):
        print('Hello')

class Minotaur(object):

    def __init__(self):
        self.phrase = Phrase()

    def say(self):
        self.phrase.say()

first_boss = Minotaur()

first_boss.say()
