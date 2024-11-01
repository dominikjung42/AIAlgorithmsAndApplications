# -*- coding: utf-8 -*-
"""
Lectorial 3 - Building a rule-based agent for credit scoring
@author: Dominik Jung (dominik.jung@jung-isec.de)
"""

#%% import python libs
from experta import *

#%% Rule-based system
class Customer(Fact):
    """ All info about the customer's credability """
    pass

class Order(Fact):
    """ Order related information like model etc. """
    pass

class Warehouse(Fact):
    """ Company information about the car production """
    pass

class CreditScoring(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Warehouse(in_stock=False)
    
    @Rule(AND(Customer(adult = True),
              Customer(fix_job = True),
              Customer(good_income = True)))
    def is_creditworthy(self):
        print("Customer is creditworthy")
        self.declare(Customer(creditworthy=True))
        
    @Rule(OR(Order(model = L("911") | L("Taycan"))))
    def can_be_produced(self):
        print("Model can be produced")
        self.declare(Warehouse(producable=True))

    @Rule(OR(Warehouse(producable = True),
             Warehouse(in_stock = True)))
    def is_available(self):
        print("Car is available")
        self.declare(Warehouse(available=True))
    
    @Rule(AND(Customer(creditworthy = True),
              Warehouse(available = True)))
    def sell_car(self):
        print("Car can be sold")
        
    @Rule(Customer(creditworthy = False))
    def sell_car(self):
        print("Customer does not fullfill all requirements")

#%% Implement scoring agent
class CreditScoringAgent():
    def inference(self):
        # We assume there is a database interface, where the agent can load the data
        engine = CreditScoring()
        engine.reset()
        
        # Example data from the data base
        engine.declare(Customer(adult=True, fix_job = True, good_income = True), Order(model = "911"))
        engine.run()

agent = CreditScoringAgent()
agent.inference()
