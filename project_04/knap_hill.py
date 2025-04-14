def reader(file_name):
    with open(file_name) as f:
        contents = f.read().splitlines()
        f.close()
        return contents


def writer(name, i, v, method):
    with open(name, 'w') as text_file:
        text_file.write('Items selected: {}\nTotal value: {}\n'.format(i, v))
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
    values = [int(i) for i in values]
    wv = [list(i) for i in zip(weights, values)]
    knap_dict = dict(zip(range(1, dimension + 1), wv))
    # print('Dictionary of knapsack items, stored in item: [weight, value] format:\n{}'.format(knap_dict))
    return knap_dict, bound


def greedy(dic, bound):
    ratio = {k: (float(v[1]/v[0])) for (k, v) in dic.items()}
    sack = {}
    for key, value in sorted(ratio.items(), key=lambda kv: kv[1], reverse=True):
        sack[key] = dic[key][0]
        if sum(sack.values()) >= bound:
            del sack[key]
            break
    for i in sack:
        sack[i] = dic[i][1]
    return list(sack.keys()), sum(sack.values())


def find_neighbours(full, solution):
    n = {key: [0] * len(full) for key in full}
    for i in n:
        for j in solution:
            n[i][j-1] = 1
        if n[i][i-1] == 1:
            n[i][i-1] = 0
        else:
            n[i][i-1] = 1
    return n


def hill(full, solution, bound):
    n = find_neighbours(full, solution)
    s = [0] * len(full)
    for i in solution:
        s[i-1] = 1
    # best improvement method
    for i in range(1, len(n)+1):
        v = val(n.get(i), full, bound)
        if v > val(s, full, bound):
            # print('new and old', v, val(s, full, bound))  # debugging print
            s = n.get(i)
    sol = []
    for i in range(len(s)):
        if s[i] == 1:
            sol.append(i+1)
    return sol, val(s, full, bound)


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


def prompt():
    iterate = input('Enter number of iterations for Hill Climbing method: ')
    try:
        iterate = int(iterate)
    except ValueError:
        iterate = 10
        print('Invalid value. Default dimension size selected:', iterate)
    return iterate


data, limit = read_knap_data('knap_test.txt')
items, total = greedy(data, limit)
writer('knap_greed_sol.txt', items, total, 'Greedy construction')
t = prompt()
print('Constructing improved solution using Hill Climbing method, please wait...')
for it in range(t):
    items, total = hill(data, items, limit)
    # print(it)  # debugging print
writer('knap_hill_sol.txt',  items, total, 'Hill climbing improvement')

