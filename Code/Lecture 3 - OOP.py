# -*- coding: utf-8 -*-
"""
Lecture 3 - Introduction into AI Programming with Python
@author: Dominik Jung (dominik.jung42@gmail.com)
"""

class Porsche:
    # Class attribute
    type = "718"
    
    # Constructor
    def __init__(self, owner):
        self.owner = owner

    # Instance method
    def speak(self):
        return ("{} says: Hello {}!".format(self.type, self.owner))


my_car = Porsche("Dominik")
my_car.owner

my_car.speak()
