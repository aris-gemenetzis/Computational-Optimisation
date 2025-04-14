# this program reads five test instances of tsp, vrp, knapsack, jobshop and p-median problems from .txt files
# the program parses each problem and prints the problem variables on the console


def reader(file_name):
    with open(file_name) as f:
        contents = f.read().splitlines()
        f.close()
        return contents


def read_tsp_data(tsp_file):
    data = reader(tsp_file)
    for i in data:
        if i.startswith('DIMENSION : '):
            dimension = int(i[i.find('DIMENSION : ') + len('DIMENSION : '):])
        if i.startswith('EDGE_WEIGHT_TYPE : '):
            e_type = i[i.find('EDGE_WEIGHT_TYPE : ') + len('EDGE_WEIGHT_TYPE : '):].strip()
        if i.startswith('CAPACITY : '):
            cap = int(i[i.find('CAPACITY : ') + len('CAPACITY : '):])
        if i.startswith('NODE_COORD_SECTION'):
            break
    data = data[data.index('NODE_COORD_SECTION') + 1:]
    print('This is a tsp problem with size {} and edge weight type {}.'.format(dimension, e_type))
    nodes = []
    for i in data:
        if not (i[0].isdigit()):
            break
        index, trash, xy = i.partition(' ')
        nodes.append(xy.split())
    # print('list of tsp node coordinates:\n{}'.format(nodes))
    tsp_dict = dict(zip(range(1, dimension + 1), nodes))
    print('Dictionary of tsp nodes and their coordinate values:\n{}\n'.format(tsp_dict))


def read_vrp_data(vrp_file):
    data = reader(vrp_file)
    for i in data:
        if i.startswith('DIMENSION : '):
            dimension = int(i[i.find('DIMENSION : ') + len('DIMENSION : '):])
        if i.startswith('EDGE_WEIGHT_TYPE : '):
            e_type = i[i.find('EDGE_WEIGHT_TYPE : ') + len('EDGE_WEIGHT_TYPE : '):].strip()
        if i.startswith('CAPACITY : '):
            cap = int(i[i.find('CAPACITY : ') + len('CAPACITY : '):])
        if i.startswith('NODE_COORD_SECTION'):
            break
    data = data[data.index('NODE_COORD_SECTION ') + 1:]
    print('This is a vrp problem with size {}, edge weight type {}, and capacity of {}.'.format(dimension, e_type, cap))
    # print(data) # debugging print
    nodes = []
    for i in data:
        if not (i[0].isdigit()):
            break
        index, trash, xy = i.partition(' ')
        nodes.append(xy.split())
    # print('list of vpr node coordinates:\n{}'.format(nodes))
    data = data[data.index('DEMAND_SECTION ') + 1:]
    # print(data) # debugging print
    demand = []
    for i in data:
        if not (i[0].isdigit()):
            break
        index, trash, d = i.partition(' ')
        demand.append(d.strip())
    # print('list of demand quantities for each vpr node:\n{}'.format(demand))
    temp = [list(i) for i in zip(nodes, demand)]
    vrp_dict = dict(zip(range(1, dimension + 1), temp))
    print('Dictionary of vrp nodes, their coordinate values and their demand:\n{}\n'.format(vrp_dict))


def read_knap_data(knap_file):
    data = reader(knap_file)
    # print(data)  # debugging print
    dimension = int(data[0])
    weights = data[1].split()
    values = data[2].split()
    bound = int(data[-1])
    print('This is a knapsack problem with size {} and bound {}.'.format(dimension, bound))
    # print('The list of weights for each item is:\n{}'.format(weights))
    # print('The list of values for each item is:\n{}'.format(values))
    wv = [list(i) for i in zip(weights, values)]
    # print(wv) # debugging print
    knap_dict = dict(zip(range(1, dimension + 1), wv))
    print('Dictionary of knapsack values and their weights:\n{}\n'.format(knap_dict))


def read_jobs_data(jobs_file):
    data = reader(jobs_file)
    info = data[1].split()
    # print(info) # debugging print
    n_jobs = int(info[0])
    n_mach = int(info[1])
    print('This is a jobshop problem with {} jobs and {} machines.'.format(n_jobs, n_mach))
    times = data[3:n_jobs+3]
    times = [i.split() for i in times]
    # print('The list of processing time on each machine for each job is:\n{}'.format(times))
    mach_order = data[-n_jobs:]
    mach_order = [i.split() for i in mach_order]
    # print('The machine processing order for each job is:\n{}'.format(mach_order))
    temp_list = [list(i) for i in zip(times, mach_order)]
    jobs_dict = dict(zip(range(1, n_jobs + 1), temp_list))
    print('Dictionary of jobs, with the machine eta and order for each job:\n{}\n'.format(jobs_dict))


def read_pemdian_data(pmedian_file):
    data = reader(pmedian_file)
    info = data[0].split()
    n_loc = info[0]
    n_edges = info[1]
    n_subset = info[-1]
    print('This is a p-median problem with {} locations, {} edges and subset size {}.'.format(n_loc, n_edges, n_subset))
    data = data[1:]
    # print(data) # debugging print
    temp_list = [i.split() for i in data]
    # print(temp_list) # debugging print
    pmedian_dict = dict(zip(range(1, len(temp_list) + 1), temp_list))
    print('Dictionary of locations, with the edge value for each set:\n{}\n'.format(pmedian_dict))


read_tsp_data('test.tsp.txt')
read_vrp_data('test.vrp.txt')
read_knap_data('test.knap.txt')
read_jobs_data('test.jobs.txt')
read_pemdian_data('test.pmedian.txt')