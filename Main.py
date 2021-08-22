import random
from GeneratePopulation import Generate_Initial_Population
from Mutation import Mutation_Function
from Crossover import Crossover_Function
from Selection import Selection_Function
from Fitness import Cost_Function
from utils import *

import sys


# genetic rep of solution
chromosome = [1, 2, 3, 4, 5] # where index == location and chromosome[index] == facility

fitness_score = 700 # cost function for this particular chromosome

data = [[chromosome], fitness_score] # data is a list containing chromosome and fitness score



def GeneticAlgorithm(problem_size, population_size, distances, flows, number_of_iterations):

    # Get dictionary that generates random value for flows and distance between locations and facilities
    #distances = Generate_Distance_Or_Flow(problem_size, 30)
    #flows = Generate_Distance_Or_Flow(problem_size, 4)


    # generate initial population
    population = Generate_Initial_Population(problem_size, population_size)

    
    solution = int(sys.maxsize)
    next_generation = []
    n = 0


    while n < number_of_iterations:

        # get cost function for each data in population
        population = Cost_Function(population=population, distances=distances, flows=flows)

        # sort population according to fitness score
        population.sort(key = lambda x: x[1])

        # get fittest data
        fittest_data = list.copy(population[0])


        # check for the fittest data and print it out
        if fittest_data[1] < solution:
            result = list.copy(fittest_data)
            solution = fittest_data[1]
            print("\nSolution for iteration - " + str(n))
            print(result)


        while len(next_generation) < len(population):

            # use selection fucntion to get 2 fit chromosomes
            data1 = Selection_Function(population)
            data2 = Selection_Function(population)

            # crossover the 2 chromosome
            crossed_over_data = Crossover_Function(data1, data2)

            # mutate both chromosomes
            offspring1 = Mutation_Function(crossed_over_data[0])
            offspring2 = Mutation_Function(crossed_over_data[1])

            # add offsprings to next generation
            next_generation.append(offspring1)
            next_generation.append(offspring2)

        # repeat iteration with new generation
        population = next_generation
        next_generation = []
        n+=1
    
    
    # print final result
    print("Final solution after " + str(n) +" iterations = ")
    print(result)

    return result
    

# helper function to help generate random distance and flow values
distances = Generate_Distance_Or_Flow(6, 20)
flows = Generate_Distance_Or_Flow(6, 4)

# Test run an exmaple with input size of 6, population size of 30 and to perform 1000 iterations
GeneticAlgorithm(6, 30, distances, flows, 1000)