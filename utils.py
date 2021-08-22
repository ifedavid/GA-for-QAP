import random

def Generate_Distance_Or_Flow(size, upper_bound) -> dict:
    """Generate random values for distance and flows between location and facilities

    Parameters
    ----------
    size : int
        The length of location/facility
    value_range : int
        The upper bound for the value of distance/flow

    Returns
    -------
    dictionary
        a dictionary where key == tuple of location/facility mapping and value == integer value of distance/flow for 
        that mapping
    """

    dictionary = {}
    for i in range(size):
        for j in range(size):
            
            if i == j: dictionary[i,j] = 0

            # since problem is a one-one problem, mapping (1,2) == (2,1) so there's no need to create duplicate mappings
            if (j,i) in dictionary: continue
            
            dictionary[i,j] = random.randrange(0, upper_bound)

    return dictionary


def Get_Distance_Or_Flow(i, j, dictionary) -> int:
    """return distance or flow value based on mapping (i, j)

    Parameters
    ----------
    i : int
        first location/facilty
    j : int
        second location/facility
    dictionary : dict
        dicttionary to search

    Returns
    -------
    int
        integer value from dictionary based on mapping (i, j)
    """

    if (i, j) not in dictionary:
        return dictionary[j, i]
    
    return dictionary[i, j]



def Chromosome_Cost(chromosome, distances, flows):
    """Gets the fitness score for a particular chromosome using the formula minϕ∈Sn ∑ni=1 ∑nj=1 fij⋅dϕ(i)ϕ(j)

    Parameters
    ----------
    chromsome : list
        list of values
    distances : list
        list of distance mapping for each data in the population
    flows : list
        list of flow mappings for each data in the population

    Returns
    -------
    int
        return cost for particular chromosome
    """
    searched_list = []
    cost = 0
    
    for j in chromosome:
            for k in chromosome:

                # since problem is a 1-1 type, mapping (1,2) == (2,1).
                if (k, j) in searched_list or (j, k) in searched_list: continue

                # cost = cost + flow(f1, f2) * distance(d1, d2) for every f1, f2, d1, d2.
                cost += Get_Distance_Or_Flow(j,k, distances) * Get_Distance_Or_Flow(chromosome[j], chromosome[k], flows)

                # append mapping to searched list to save time.
                searched_list.append((j, k))
    
    return cost


#flows = {(0,0) : 2, (0, 1) : 3, (0, 2): 0, (0, 3): 2, (1, 1): 0, (1,2):0, (1,3): 1, (2, 2): 0, (2, 3): 4, (3,3):0}
#distances = {(0,0): 0, (0, 1): 22, (0, 2): 53, (0, 3): 53, (1, 1): 0, (1, 2): 40, (1, 3): 62, (2, 2): 0, (2, 3): 55, (3, 3): 0}
