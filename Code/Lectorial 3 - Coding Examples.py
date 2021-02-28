# -*- coding: utf-8 -*-
"""
Lectorial 3 - Building a rule-based agent for credit scoring
@author: Dominik Jung (dominik.jung42@gmail.com)
"""
from experta import *

# Facts in experta
my_car = Fact(model="911 Turbo", horsepower=572)
print(my_car["model"])

# Work with facts
class Status(Fact):
    pass

my_fact = Status(color = "red")
print(my_fact)

# DefFacts
@DefFacts()
def needed_data():
    yield Fact(car_color="red")
    yield Fact(price=170000)

# Rules
class my_fact(Fact):
    pass

@Rule(my_fact())
def matchWithEveryMyFact():
    pass

@Rule(my_fact(my_car=911))
def is_happy():
    print("I am happy!")

# variable binding
@Rule(Fact("car" << W()))
def foo(value):
    pass

# knowledge engine
class helloWorld(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="say_hello")
    
    @Rule(Fact(action="say_hello"), NOT(Fact(name=W())))
    def ask_name(self):
        self.declare(Fact(name=input("Hey, what's your name? ")))
    
    @Rule(Fact(action="say_hello"), Fact(name="name" << W()))
    def greet(self,  name):
        print("Hi ", name)

engine = helloWorld()
engine.reset()
engine.run()

engine.facts











