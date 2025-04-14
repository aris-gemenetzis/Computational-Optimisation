def reader(file_name):
    with open(file_name) as f:
        contents = f.read().splitlines()
        f.close()
        return contents


def writer(name, i, v, method):
    with open(name, 'w') as text_file:
        text_file.write('Items selected: {}\nTotal value: {}\n'.format(i, v))
    print('{} construction result stored in file: {}'.format(method, name))


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
    values = [int(i) for i in values]
    wv = [list(i) for i in zip(weights, values)]
    knap_dict = dict(zip(range(1, dimension + 1), wv))
    print('Dictionary of knapsack items, described by their weights and values:\n{}'.format(knap_dict))
    return knap_dict, bound


def greedy(dic, bound):
    ratio = {k: (float(v[1]/v[0])) for (k, v) in dic.items()}
    # print(ratio)  # debugging print
    sack = {}
    for key, value in sorted(ratio.items(), key=lambda kv: kv[1], reverse=True):
        sack[key] = dic[key][0]
        if sum(sack.values()) >= bound:
            del sack[key]
            break
    for i in sack:
        sack[i] = dic[i][1]
    # print(len(sack), sum(sack.values()))  # debugging print
    return list(sack.keys()), sum(sack.values())


data, limit = read_knap_data('knap.txt')
items, total = greedy(data, limit)
writer('knap_greed_sol.txt', items, total, 'Greedy')
