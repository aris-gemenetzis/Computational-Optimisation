import random


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
    print('Dictionary of knapsack items, stored in item: [weight, value] format:\n{}'.format(knap_dict))
    return knap_dict, bound


def construction(dic, bound, n):
    ratio = {k: (float(v[1]/v[0])) for (k, v) in dic.items()}
    sack = {}
    objects = sorted(ratio.items(), key=lambda kv: kv[1], reverse=True)
    for key, value in objects:
        rcl = objects[:n]
        s = objects.pop(random.choice(range(len(rcl))))
        sack[s[0]] = dic.get(s[0])[0]
        if sum(sack.values()) >= bound:
            del sack[key]
            break
    for i in sack:
        sack[i] = dic.get(i)[1]
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
            # break  # uncomment for first improvement method
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


# user input prompts
def prompt():
    iterate = []
    defaults = [10, 3, 10]
    prompts = ['number of iterations for GRASP method', 'size of RCL list', 'number of iterations for local search']
    for i in range(len(prompts)):
        user_input = input('Enter {}: '.format(prompts[i]))
        try:
            iterate.append(int(user_input))
        except ValueError:
            iterate.append(defaults[i])
            print('Invalid value. Default {} selected: {}'.format(prompts[i], defaults[i]))
    return iterate


def grasp(full, bound, g, h, n):
    final = (None, 0)
    for i in range(g):
        # grasp phase one
        solution, value = construction(full, bound, n)
        # print(value)  # debugging print
        # grasp phase two
        for j in range(h):
            solution, value = hill(full, solution, bound)
            if value > final[1]:
                final = (solution, value)
            # print(j, value, final[1])  # debugging print
    # print(final)  # debugging print
    return final[0], final[1]


data, limit = read_knap_data('knap_test.txt')
t = prompt()
print('Constructing improved solution using GRASP method, please wait...')
items, total = grasp(data, limit, t[0], t[1], t[2])
writer('knap_grasp_sol.txt', items, total, 'GRASP solution')
