from utils import Get_Distance_Or_Flow


# cost function to get cost of each chromosome
def Cost_Function(population, distances, flows) -> list:
    """Gets the fitness score for each data in a population using the formula minϕ∈Sn ∑ni=1 ∑nj=1 fij⋅dϕ(i)ϕ(j)

    Parameters
    ----------
    population : list
        list of data
    distances : list
        list of distance mapping for each data in the population
    flows : list
        list of flow mappings for each data in the population

    Returns
    -------
    list
        list of data with updated fitness score
    """
    for data in population:

        cost = 0

        searched_list = []

        for j in data[0]:
            for k in data[0]:

                # since problem is a 1-1 type, mapping (1,2) == (2,1).
                if (k, j) in searched_list or (j, k) in searched_list: continue

                # cost = cost + flow(f1, f2) * distance(d1, d2) for every f1, f2, d1, d2.
                cost += Get_Distance_Or_Flow(j,k, distances) * Get_Distance_Or_Flow(data[0][j], data[0][k], flows)

                # append mapping to searched list to save time.
                searched_list.append((j, k))


        data[1] = cost

    #print("/nPopulation with fitness score for each chromosome - ")
    #print(population)

    return population


