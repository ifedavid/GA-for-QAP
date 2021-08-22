import random

# selection function
def Selection_Function(population) -> list:
    """Select data with the minimum fitness score from a population using the tournament selection technique

    Parameters
    ----------
    population : list
        list of data

    Returns
    -------
    list
        data with the minimum fitness score from the population
    """

    # return random list size population_size/5 from population 
    random_k_list = random.sample(population, int(len(population)/5))

    # sort random list using their fitness score 
    random_k_list.sort(key = lambda x: x[1])
    
    #print("Fittest chromosome - ")
    #print(random_k_list[0])

    # return first element after sort
    return random_k_list[0]





