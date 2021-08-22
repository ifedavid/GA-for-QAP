import random

# function to generate new population 
def Generate_Initial_Population(problem_size, population_size) -> list:
    """Generate list of random data

    Parameters
    ----------
    problem_size : int
        size of the problem i.e no of location/facilites

    population_size : int
        number of data we want in our list 

    Returns
    -------
    list
        return list of data
    """

    population = []

    for i in range (population_size):

        # create list with size == problem size and random values ranging from 0 - problem_size
        x = random.sample(range(problem_size), problem_size)
        population.append([x, 0])
    
    #print("Initial Population - ")
    #print(population)
    
    return population

