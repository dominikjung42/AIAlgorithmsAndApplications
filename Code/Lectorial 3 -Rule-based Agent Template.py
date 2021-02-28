# -*- coding: utf-8 -*-
"""
Lectorial 3 - Building a rule-based agent for credit scoring
@author: Dominik Jung (dominik.jung42@gmail.com)
"""

#%% import python libs
from experta import *

#%% Knowledge engine and rule base
class CreditScoring(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        pass
    
    @Rule(..)

#%% Implement scoring agent
class CreditScoringAgent():
    def inference(self):
        pass

agent = CreditScoringAgent()
agent.inference()