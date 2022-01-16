# -*- coding: utf-8 -*-
"""
Lectorial 1 - Implementing Simple Reflex Agent
@author: Dominik Jung (dominik.jung42@gmail.com)
"""
#%% Imports
import numpy

#%% 1. Define variables
vacuum_world = {"Bedroom":[["Living room"], False],
                "Living room":[["Bedroom", "Bathroom"], False],
                "Bathroom":[["Living room"], True]}

start_room = "Bedroom"
print(vacuum_world[start_room][1])

#%% 2. Vacuum Cleaner
class Cleaner:
    name = "Dobby"
    energy = 5
    
    def __init__(self, room, world):
        self.location = room
        self.world = world

    # cost function
    def power_consumption(self):
        self.energy = self.energy - 1

    # perception
    def percepts(self):
        is_dirty = self.world[self.location][1]
        self.act(is_dirty)

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
    
    def act(self, is_dirty):
        if(is_dirty == True):
            self.suck()
            print("Room {} is dirty, clean room".format(self.location))
        else:
            print("Room {} is clean".format(self.location))
            self.drive()
        
        print("Energy left: {}".format(self.energy))
        if(self.energy <= 1):
            self.location = "Bedroom"
            print("Return to docking station: Abort cleaning.")

#%% 3. Simulation
dobby = Cleaner(room = "Bedroom", world = vacuum_world)
print("\nStarting to clean!")

stop = False
while stop != True:
    world_status = dobby.world.values()
    
    num_dirty_rooms = 0
    for room in world_status:
        dirty_rooms = []
        dirty_rooms.append(room[1])
        num_dirty_rooms = sum(dirty_rooms)
    print("Dirty rooms: {}".format(num_dirty_rooms))
    
    if(num_dirty_rooms > 0 and dobby.energy > 1):
        dobby.percepts()
    else:
        print("Finished cleaning")
        stop = True
        

