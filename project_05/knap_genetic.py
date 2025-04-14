import random


def reader(file_name):
    with open(file_name) as f:
        contents = f.read().splitlines()
        f.close()
        return contents


def writer(name, i, value, method):
    with open(name, 'w') as text_file:
        text_file.write('Items selected: {}\nTotal value: {}\n'.format(i, value))
    print('{} result stored in file: {}'.format(method, name))


def read_knap_data(knap_file):
    text = reader(knap_file)
    dimension = int(text[0])
    weights = text[1].split()
    values = text[2].split()
    bound = int(text[-1])
    print('This is a knapsack problem with size {} and bound {}.'.format(dimension, bound))
    # print('The list of weights for each item is:\n{}'.format(weights))
    # print('The list of values for each item is:\n{}'.format(values))
    weights = [int(i) for i in weights]
    value = [int(i) for i in values]
    wv = [list(i) for i in zip(weights, value)]
    knap_dict = dict(zip(range(1, dimension + 1), wv))
    print('Dictionary of knapsack items, stored in item: [weight, value] format:\n{}'.format(knap_dict))
    return knap_dict, bound


# generates a random valid solution
def rnd(dic, bound):
    sack = {}
    while True:
        s = random.choice(list(dic.keys()))
        sack[s] = dic.get(s)[0]
        if sum(sack.values()) >= bound:
            del sack[s]
            break
    for s in sack:
        sack[s] = dic[s][1]
    return list(sack.keys())


# turns an item list with integer values
# into a binary item list
def encode(lst, n):
    b = [0] * n
    for i in lst:
        b[i-1] = 1
    return b


# turns a binary item list
# into an item list with integer values
def decode(lst):
    items = [i+1 for i in range(len(lst)) if lst[i] == 1]
    return items


# evaluation function
def val(solution, full, bound):
    v, w = 0, 0
    for i in range(len(solution)):
        if solution[i] == 1:
            w += full[i+1][0]
            v += full[i+1][1]
    if w > bound:
        return -1
    else:
        return v


# user input prompt
def prompt():
    n = input('Enter initial population size: ')
    try:
        n = int(n)
    except ValueError:
        n = 10
        print('Invalid value. Default population size selected:', n)
    iterate = input('Enter number of iterations for Genetic algorithm: ')
    try:
        iterate = int(iterate)
    except ValueError:
        iterate = 10
        print('Invalid value. Default number selected:', iterate)
    return iterate, n


# randomly generates first set of parents
def first(ti, dat, lim):
    par = []
    for i in range(ti):
        rand = rnd(dat, lim)
        par.append(encode(rand, len(dat)))
    return par


# 1-point crossover
def crossover(par):
    chi = []
    for p in range(0, len(par), 2):
        c1 = par[p][:int(len(par[p])/2)]+par[p+1][int(len(par[p])/2):]
        c2 = par[p+1][:int(len(par[p])/2)]+par[p][int(len(par[p])/2):]
        chi.extend((c1, c2))
    return chi


# flip bit mutation
def mutation(people):
    for p in people:
        for gene in range(len(p)):
            if random.random() < 0.01:
                p[gene] = 1 - p[gene]
    return people


# replace worst
def selection(people, n, dat, lim):
    values = {i: val(people[i], dat, lim) for i in range(len(people))}
    for s in range(n):
        v = min(values, key=lambda x: values.get(x))
        values.pop(v, None)
    people = [people[i] for i in range(len(people)) if i in values.keys()]
    return people


# find best solution
def best(people, dat, lim):
    values = {i: val(people[i], dat, lim) for i in range(len(people))}
    m = max(values, key=lambda x: values.get(x))
    return people[m]


def genetic(ti, dat, lim, n):
    population = first(n, dat, lim)
    for i in range(ti):
        children = crossover(population)
        population = population + children
        population = mutation(population)
        population = selection(population, n, dat, lim)  # new population
    solution = best(population, dat, lim)
    return solution


data, limit = read_knap_data('knap_test.txt')
iterations, size = prompt()
gen_sol = genetic(iterations, data, limit, size)
writer('knap_gen_sol.txt', decode(gen_sol), val(gen_sol, data, limit), 'Genetic solution')  #

