import math


def read_file():
    graph = []
    for line in open("input_10.txt").read().split("\n"):
        graph.append(line.split())
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            graph[i][j] = int(graph[i][j])
            if graph[i][j] == 0 and i != j:
                graph[i][j] = math.inf
    return graph


def start():
    G = read_file()
    N = len(G)
    result = [math.inf] * N
    point = int(input("start point: ")) - 1
    finish = int(input("finish point:")) - 1
    Viewed = [point]
    result[point] = 0
    while point != -1:
        for i, distanse in enumerate(G[point]):  # перебор всех соседей v
            if i not in Viewed:
                value = result[point] + distanse
                if value < result[i]:
                    result[i] = value
        point = choose_min(result, Viewed)
        if point >= 0:
            Viewed.append(point)
    print("result: ", result[finish])


def choose_min(result, Viewed):
    minimum = -1
    maximum = math.inf
    for i, t in enumerate(result):
        if t < maximum and i not in Viewed:
            maximum = t
            minimum = i
    return minimum


start()
