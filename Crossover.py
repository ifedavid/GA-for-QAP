import random
from iteration_utilities import duplicates


# crossover function
def Crossover_Function(data1, data2):
    """Perform modified version of uniform crossover on 2 chromosomes

    Parameters
    ----------
    data1 : list
        data list containing chromosome and fitness score
    data2 : list
        data list containing chromosome and fitness score

    Returns
    -------
    list
        return list containing 2 data with modified chromosome
    """

    # for this function, I modified the uniform crossover function to take care of duplicates after crossover.

    data1[1] = 0
    data2[1] = 0
    chromosome1 = list.copy(data1[0])
    chromosome2 = list.copy(data2[0])

    #print("\nChromosomes before crossover - ")
    #print(chromosome1)
    #print(chromosome2)

    # for each index in both chromosomes, use a coin toss to determine which index is crossed over
    for i in range(len(chromosome1)):

        cointoss = random.randrange(2)
        if cointoss == 0:
            chromosome1[i], chromosome2[i] = chromosome2[i], chromosome1[i]

    # find duplicates after crossing over
    dupes_in_ch1 = list(duplicates(chromosome1))
    dupes_in_ch2 = list(duplicates(chromosome2))


    # handle duplicates if any are found
    for i in dupes_in_ch1:
        if i in chromosome1: chromosome1.remove(i)
        chromosome2.append(i)
    
    for i in dupes_in_ch2:
        if i in chromosome2: chromosome2.remove(i)
        chromosome1.append(i)

    # replaced the modified chromosomes in the data
    data1[0] = chromosome1
    data2[0] = chromosome2

    #print("\nChromsomes after crossover - ")
    #print(data1[0])
    #print(data2[0])

    return [data1, data2]


