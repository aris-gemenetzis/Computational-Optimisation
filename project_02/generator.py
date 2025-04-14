# this program generates problem instances for tsp, vrp, knapsack, jobshop and p-median problem types
# the program receives user input for crucial problem parameters, reverting to default values if user input is invalid
# for certain parameters the user has the ability to define a specific value range, whereas
# for others -such as demand, time, or weight- only the maximum desired value is required since the value range
# in those cases is expected to start from zero
# the corresponding problem is then generated and stored in an appropriately titled .txt file

import random


def tsp_generator():
    print('Generating tsp problem...')
    dim = input('Enter problem dimension: ')
    try:
        dim = int(dim)
        # print('Input dimension value is:', dim)  # debugging print
    except ValueError:
        dim = 50
        print('Invalid value. Default dimension size selected:', dim)
    low = input('Enter coordinate min value: ')
    try:
        low = int(low)
        # print('Input min value is:', low)  # debugging print
    except ValueError:
        low = 10
        print('Invalid value. Default min value selected:', low)
    high = input('Enter coordinate max value: ')
    try:
        high = int(high)
        # print('Input max value is:', high)  # debugging print
    except ValueError:
        high = 5000
        print('Invalid value. Default max value selected:', high)
    e_type = input('Enter edge weight type: ')
    e_type = e_type.upper()
    with open('tsp_gen.txt', 'w') as text_file:
        text_file.write('TYPE : TSP\nDIMENSION : {}\nEDGE_WEIGHT_TYPE : {} \nNODE_COORD_SECTION\n'.format(dim, e_type))
    with open('tsp_gen.txt', 'a') as text_file:
        for i in range(1, dim+1):
            x = random.randrange(min(low, high), max(low, high)+1)  # min() & max() function use
            y = random.randrange(min(low, high), max(low, high)+1)  # safeguards the program from user input error
            text_file.write('{} {} {}\n'.format(i, x, y))
        text_file.write('EOF')


def vrp_generator():
    print('Generating vrp problem...')
    dim = input('Enter problem dimension: ')
    try:
        dim = int(dim)
        # print('Input dimension value is:', dim)  # debugging print
    except ValueError:
        dim = 50
        print('Invalid value. Default dimension size selected:', dim)
    low = input('Enter coordinate min value: ')
    try:
        low = int(low)
        # print('Input min value is:', low)  # debugging print
    except ValueError:
        low = 10
        print('Invalid value. Default min value selected:', low)
    high = input('Enter coordinate max value: ')
    try:
        high = int(high)
        # print('Input max value is:', high)  # debugging print
    except ValueError:
        high = 5000
        print('Invalid value. Default max value selected:', high)
    dem = input('Enter max demand: ')
    try:
        dem = int(dem)
        # print('Input max demand value is:', dem)  # debugging print
    except ValueError:
        dem = 30
        print('Invalid value. Default max demand value selected:', dem)
    cap = input('Enter vehicle capacity: ')
    try:
        cap = int(cap)
        # print('Input capacity value is:', cap)  # debugging print
    except ValueError:
        cap = 100
        print('Invalid value. Default capacity value selected:', cap)
    e_type = input('Enter edge weight type: ')
    e_type = e_type.upper()
    with open('vrp_gen.txt', 'w') as text_file:
        text_file.write('TYPE : VRP\nDIMENSION : {}\nEDGE_WEIGHT_TYPE : {} \nCAPACITY : {}\nNODE_COORD_SECTION\n'.format(dim, e_type, cap))
    with open('vrp_gen.txt', 'a') as text_file:
        for i in range(1, dim + 1):
            x = random.randrange(min(low, high), max(low, high) + 1)  # min() & max() function use
            y = random.randrange(min(low, high), max(low, high) + 1)  # safeguards the program from user input error
            text_file.write('{} {} {}\n'.format(i, x, y))
        text_file.write('DEMAND_SECTION\n')
        for i in range(1, dim + 1):
            d = random.randrange(0, dem + 1)
            text_file.write('{} {}\n'.format(i, d))
        text_file.write('DEPOT_SECTION\n1\n-1\nEOF')


def knapsack_generator():
    print('Generating knapsack problem...')
    # programmer's note: this function aims to emulate the format of knapsack problem instance files found online,
    # similar to those used for the previous project (parser).
    # hence there are no explicit identifiers preceding aspects like dimension, item weight, or item value
    # in the resulting file, since the data of the original instances were also stored in raw, unlabelled form
    dim = input('Enter problem dimension: ')
    try:
        dim = int(dim)
        # print('Input dimension value is:', dim)  # debugging print
    except ValueError:
        dim = 50
        print('Invalid value. Default dimension size selected:', dim)
    w_max = input('Enter max weight value: ')
    try:
        w_max = int(w_max)
        # print('Input  max weight value is:', w_max)  # debugging print
    except ValueError:
        w_max = 500
        print('Invalid value. Default max weight selected:', w_max)
    low = input('Enter min item value: ')
    try:
        low = int(low)
        # print('Input min value is:', low)  # debugging print
    except ValueError:
        low = 100
        print('Invalid value. Default min value selected:', low)
    high = input('Enter max item value: ')
    try:
        high = int(high)
        # print('Input max value is:', high)  # debugging print
    except ValueError:
        high = 1000
        print('Invalid value. Default max value selected:', high)
    bound = input('Enter knapsack bound: ')
    try:
        bound = int(bound)
        # print('Input bound value is:', bound)  # debugging print
    except ValueError:
        bound = 100
        print('Invalid value. Default bound value selected:', bound)
    with open('knapsack_gen.txt', 'w') as text_file:
        text_file.write('{}\n'.format(dim))
    with open('knapsack_gen.txt', 'a') as text_file:
        for i in range(1, dim + 1):
            w = random.randrange(w_max + 1)
            text_file.write('{} '.format(w))
        text_file.write('\n')
        for i in range(1, dim + 1):
            v = random.randrange(min(low, high), max(low, high) + 1)  # min() & max() functions used as a precaution
            text_file.write('{} '.format(v))
        text_file.write('\n{}'.format(bound))


def jobshop_generator():
    print('Generating jobshop problem...')
    jobs = input('Enter number of jobs: ')
    try:
        jobs = int(jobs)
        # print('Input jobs value is:', jobs)  # debugging print
    except ValueError:
        jobs = 10
        print('Invalid value. Default job number selected:', jobs)
    machs = input('Enter number of machines: ')
    try:
        machs = int(machs)
        # print('Input machines value is:', machs)  # debugging print
    except ValueError:
        machs = 5
        print('Invalid value. Default machine number selected:', machs)
    t_max = input('Enter max job time: ')
    try:
        t_max = int(t_max)
        # print('Input max time value is:', t_max)  # debugging print
    except ValueError:
        t_max = 100
        print('Invalid value. Default dimension size selected:', t_max)
    with open('jobshop_gen.txt', 'w') as text_file:
        text_file.write('nb_jobs nb_machines\n{} {} 0 0 0 \nTimes\n'.format(jobs, machs))
    with open('jobshop_gen.txt', 'a') as text_file:
        for i in range(jobs):
            for j in range(machs):
                t = random.randrange(t_max + 1)
                text_file.write('{} '.format(t))
            text_file.write('\n')
        text_file.write('Machines\n')
        # print(m_list)  # debugging print
        for i in range(jobs):
            m_list = [i for i in range(1, machs + 1)]
            while m_list:
                m = random.choice(m_list)
                m_list.remove(m)
                # print(m)  # debugging print
                # randomly generating a machine order for each job
                text_file.write('{} '.format(m))
            text_file.write('\n')


def pmedian_generator():
    # programmer's note: this function aims to emulate the format of p-median problem instance files found online,
    # similar to those used for the previous project (parser).
    # hence there are no explicit identifiers preceding aspects like location number, edge number, or edge weight value
    # in the resulting file, since the data of the original instances were also stored in raw, unlabelled form
    print('Generating a p-median problem...')
    locations = input('Enter number of locations: ')
    try:
        locations = int(locations)
        # print('Input location number value is:', locations)  # debugging print
    except ValueError:
        locations = 10
        print('Invalid value. Default location number selected:', locations)
    edges = input('Enter number of edges: ')
    try:
        edges = int(edges)
        # print('Input edges value is:', edges)  # debugging print
    except ValueError:
        edges = 20
        print('Invalid value. Default edge number selected:', edges)
    p = input('Enter p value: ')
    try:
        p = int(p)
        # print('Input p value is:', p)  # debugging print
    except ValueError:
        p = 5
        print('Invalid value. Default p value selected:', p)
    w_max = input('Enter max edge weight: ')
    try:
        w_max = int(w_max)
        # print('Input max edge weight value is:', w_max)  # debugging print
    except ValueError:
        w_max = 500
        print('Invalid value. Default max weight selected:', w_max)
    with open('p-median_gen.txt', 'w') as text_file:
        text_file.write('{} {} {}\n'.format(locations, edges, p))
    with open('p-median_gen.txt', 'a') as text_file:
        for i in (range(locations)):
            for j in range(locations):
                w = random.randrange(w_max + 1)
                text_file.write('{} '.format(w))
            text_file.write('\n')


def user_input():
    options = {'tsp': tsp_generator, 'vrp': vrp_generator, 'knapsack': knapsack_generator, 'jobshop': jobshop_generator,
               'p-median': pmedian_generator}
    problem = input('Enter problem type (\'tsp\', \'vrp\', \'knapsack\', \'jobshop\' and \'p-median\': ')
    if problem in options.keys():
        print('Input problem type is: ', problem)
    else:
        print('Invalid problem value: {}. Problem type will now be randomly selected.'.format(problem))
        problem_list = ['tsp', 'vrp', 'knapsack', 'jobshop', 'p-median']
        problem = random.choice(problem_list)
    options[problem]()
    return


user_input()
# tsp_generator()  # debugging print
# vrp_generator()  # debugging print
# knapsack_generator()  # debugging print
# jobshop_generator()  # debugging print
# pmedian_generator()  # debugging print

