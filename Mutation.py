import random


# It gets 2 random indexes in the chromosome and switches their value.

def Mutation_Function(data) -> list:
    """Modifies the chromosome in a data

    Parameters
    ----------
    gene : list
        specific data that needs modification

    Returns
    -------
    list
        returns the Modified data
    """

    chromosome = data[0]

    #print("\nChromosome before modification - ")
    #print(chromosome)

    randomNum1 = random.randint(0, len(chromosome) - 1)
    randomNum2 = random.randint(0, len(chromosome) - 1)

    # exchange values at 2 random indexes
    chromosome[randomNum1], chromosome[randomNum2] = chromosome[randomNum2], chromosome[randomNum1]

    #print("\nChromosome after mutation - ")
    #print(chromosome)

    return data
