# -*- coding: utf-8 -*-
"""
Lectorial 1 - Implementing Simple Reflex Agent
@author: Dominik Jung (dominik.jung42@gmail.com)
"""
#%% Imports
import numpy

#%% 1. Define variables
vacuum_world = { "Bedroom" : [["Living room"], False],
      "Living room" : [["Bedroom","Bathroom"], False],
      "Bathroom": [["Living room"], True]}

start_room = "Bedroom"

print("Cleaning need of the start room is:", vacuum_world[start_room][1])

#%% 2. Vacuum cleaner
class Cleaner:
    name = "dobby"
    energy = 5
    
    def __init__(self, room, vacuum_world):
        self.location = room
        self.world = vacuum_world

    # cost function
    def power_consumption(self):
        self.energy = self.energy-1

    # perception
    def percepts(self, vacuum_world):
        self.world = vacuum_world
        status = self.world[self.location][1]
        self.act(status)

    # actions
    def suck(self):
        self.world[self.location][1] = False
        self.power_consumption()
    
    def drive(self):
        neigbor_rooms = self.world[self.location][0]
        num_rooms = len(neigbor_rooms)
        r = numpy.random.randint(low = 0, high = num_rooms)
        
        self.location = neigbor_rooms[r]
        print("Drive to next room: {}".format(self.location))
        self.power_consumption()
    
    def act(self, status):
        room_status = status
        if(room_status == True):
            self.suck()
            print("Room {} is dirty, clean room".format(self.location))
        else:
            print("Room {} is clean".format(self.location))
            self.drive()
            
        print("Energy left: {}".format(self.energy))
        if(self.energy <= 1):
            self.location = "Bedroom"
            print("Return to docking station.")
        
#%% Test
dobby = Cleaner("Bedroom", vacuum_world)
vacuum_world = dobby.world
dobby.percepts(vacuum_world)
vacuum_world = dobby.world
dobby.percepts(vacuum_world)

#%% 3. Simulate
dobby = Cleaner("Bedroom", vacuum_world)
stop = False

while stop != True:
    world = dobby.world
    world_status = world.values()
    
    cleaning_status=[]
    for room in world_status:
        cleaning_status.append(room[1])
        
    if(True in cleaning_status):
        dobby.percepts(world)
    else:
        print("Finished Cleaning")
        stop=True

#%%


    
    
    