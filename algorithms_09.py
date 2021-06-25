def start(s, f):
    graph = [
        [False, True, False, True, False, False, False, False, False],
        [True, False, False, True, False, True, False, False, False],
        [False, False, False, False, True, True, False, False, False],
        [True, True, False, False, True, False, True, True, False],
        [False, False, True, True, False, True, True, False, True],
        [False, True, True, False, True, False, False, True, True],
        [False, False, False, True, True, False, False, False, False],
        [False, False, False, True, False, True, False, False, True],
        [False, False, False, False, True, True, False, True, False]
    ]
    used = [s]
    result = [None] * len(graph)
    result[s] = 0
    stack = [(s, 0)]
    dfs(graph, s, result, stack, used)
    #print(result)
    print("result: ", shortest_way(graph, s, f, result))


def shortest_way(G, s, f, result, counter=0):
    key = []
    value = []
    for e in range(len(G[f])):
        if G[f][e]:
            key.append(e)
            value.append(result[e])
    f = key[value.index(min(value))]
    if result[f] == 0:
        return counter + 1
    else:
        return shortest_way(G, s, f, result, counter+1)


def dfs(G, s, result, stack, used):
    for e in range(len(G[s])):
        if G[s][e] and e not in used:
            result[e] = stack[len(stack) - 1][1] + 1
            used.append(e)
            stack.append((e, stack[len(stack) - 1][1] + 1))
            dfs(G, e, result, stack, used)
            stack.pop(len(stack) - 1)


start(int(input("start point: ")), int(input("finish point:")))
