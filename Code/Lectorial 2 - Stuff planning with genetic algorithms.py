# -*- coding: utf-8 -*-
"""
Lectorial 2 - Stuff planning with genetic algorithms
@author: Dominik Jung (dominik.jung@jung-isec.de)
"""

#%% import python libs
import numpy
import pandas
from operator import itemgetter

#%% 1. We load our employees, their working times and the capacity planning

# the staff_list consists of all worker id, start time, and maximum working time by contract for each day
staff_list = pandas.read_excel(open("db_staffplanning.xlsx", "rb"),
                  sheet_name="staff") # this kind of data is termed 'long' data

# the workload_table describes the needed capacity over the whole week
workload_table = pandas.read_excel(open("db_staffplanning.xlsx", "rb"),
                  sheet_name="workload") # this kind of data is termed 'wide' data

#%% 2. Transform from staff per hour to timetable format

# compute worker availability based on contract and start_time
def is_worker_available(staff_list, worker, day, time):
    condition = ((staff_list["ID"] == worker) & (staff_list["DAY"] == day))
    start_time = staff_list.loc[condition, "START"]
    work_time = staff_list.loc[condition, "CONTRACT"]
    end_time = start_time + work_time
    
    availability = ((time >= start_time) & (time < end_time)).item()
    
    return availability

# aggregate staff_list to planing_table to compare with workload_table
def format_staff_list(staff_list, workload_table):
    planing_table = workload_table.copy() # use workload as a template for timetable comparison
    
    for day in planing_table["DAY"]:
        for time in range(0, 25):
            workers_available = 0
            for worker in range(1, 11):
                availability = is_worker_available(staff_list, worker, day, time)
                if(availability == True):
                    workers_available = (workers_available + 1)
            planing_table.loc[(planing_table["DAY"] == day), time] = workers_available
            
    return(planing_table)
           
#%% 3. The random initialization for the evolution step

# generate new random starting times based on the conditions in the original staff_list
def generate_staff_list(staff_list):
    new_staff_list = staff_list.copy() # template
    
    for day in new_staff_list["DAY"]:
        for worker in new_staff_list["ID"]:
            condition = ((new_staff_list["ID"] == worker) & (new_staff_list["DAY"] == day))
            new_staff_list.loc[(condition), "START"] = numpy.random.randint(0, 23)
            
    return(new_staff_list)
  
#%% 4.1 Genetic steps - Generate population of parents

# generates multiple staff lists, otherwise you have to use the list from the db and starte there
def generate_staff_list_population(num_lists, staff_list):
    staff_list_population = []
    
    for i in range(num_lists):
        new_staff_list = generate_staff_list(staff_list)
        staff_list_population.append(new_staff_list)
        
    return staff_list_population

#%% 4.2 Genetic steps - Combination / Crossover

# function to combine two different start_time lists
def crossover(parents, num_childs):
    num_parents = len(parents)
    childs = []
    
    for i in range(num_childs):
        mom = parents[numpy.random.randint(low = 0, high = num_parents - 1)]
        dad = parents[numpy.random.randint(low = 0, high = num_parents - 1)]
        child = mom.copy()
        
        selection = numpy.random.choice(range(0,50), size=25, replace=False)
        child.loc[selection] = dad.loc[selection]
        childs.append(child)
        
    return childs

#%% 4.3 Genetic steps - Mutation

# mutate existing solutions
def mutate(parents, num_mutations):
    num_parents = len(parents)

    for i in range(num_parents):
        selection = numpy.random.choice(range(0,50), size=num_mutations, replace=False)
        mutations = numpy.random.randint(low = 0, high = 23, size=len(selection))
        parents[i].loc[selection, "START"] = mutations
        
    return parents

    
#%% 5. Compute fitness of the current planning

# this is the core of your genetic programm: compute fitness of a timetable compared to the workload
def fitness_function(planing_table, workload_table):
    dif = workload_table.set_index("DAY").subtract(planing_table.set_index("DAY"), fill_value=0)
    dif = dif.mask(dif < 0, 0)
    dif_sum = dif.sum(axis=1).sum(axis=0)
    
    max_workload = workload_table.set_index("DAY").sum(axis=1).sum(axis=0)
    fitness = (1 - dif_sum/max_workload)
    
    return fitness

def rank_staff_lists(staff_list_population, workload_table):
    results = []
    for individual in staff_list_population:
        planing_table = format_staff_list(individual, workload_table)
        fitness = fitness_function(planing_table, workload_table)
        results.append([fitness, individual])
    
    results = sorted(results, key=itemgetter(0), reverse=True)
        
    return(results)


#%% Genetic Algorithm
def evolution(staff_list, workload_table, num_iterations, pop_size):
    population = generate_staff_list_population(num_lists = pop_size, staff_list = staff_list)
    if(pop_size< 4):
        pop_size = 4
    
    for i in range(num_iterations):
        # compute fitness
        ranked_staff_lists = rank_staff_lists(staff_list_population = population, workload_table = workload_table)
        
        # keep only top 2
        population = []
        for j in range(2):
            population.append(ranked_staff_lists[j][1])
        
        # crossover & mutate
        childs = crossover(parents = population, num_childs = pop_size-2)
        childs = mutate(parents = childs, num_mutations = 10)
        
        # new population
        population.extend(childs)
    
    winner = rank_staff_lists(staff_list_population = population, workload_table = workload_table)[0]
    print(winner)
    
#%% Run
evolution(staff_list = staff_list, workload_table = workload_table, num_iterations = 10, pop_size=4)






