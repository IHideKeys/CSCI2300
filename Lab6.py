import heapdict


def dijkstra(G, s):
    dist = [10000000 for _ in range(len(G))]
    prev = [None for _ in range(len(G))]
    dist[s] = 0
    hd = heapdict.heapdict()
    for i in range(0, len(G)):
        hd[i] = dist[i]

    while len(hd) != 0:
        u = hd.popitem()[0]
        for i in range(0, len(G[u])):
            v = G[u][i][0]
            if int(dist[v]) > int(dist[u] + G[u][i][1]):
                dist[v] = int(dist[u] + G[u][i][1])
                prev[v] = int(u)
                hd.__setitem__(v, dist[v])

    path = []
    for i in range(0, len(prev)):
        string = str(i) + ": " + str(dist[i]) + ","
        if prev[i] is not None:
            j = prev[i]
            path.insert(0, i)
            path.insert(0, j)
            while j != s:
                j = prev[j]
                path.insert(0, j)
            print(string + str(path))
        elif prev[i] is None and i == s:
            path.append(i)
            print(str(i) + ": 0," + str(path))
        path = []


def getG(n):
    dataFile = open(n, "r")
    num_lines = sum(1 for _ in open(n))
    tempG = [[0 for _ in range(3)] for _ in range(num_lines)]
    graph = [[]]
    for i in range(0, num_lines):
        line = dataFile.readline().strip("\n")
        tokens = line.split(" ", 2)
        line.split(" ", num_lines)
        if len(tokens) > 1:
            for j in range(0, 3):
                tempG[i][j] = int(tokens[j])
    largestNode = calcMax(n)
    for i in range(0, largestNode):
        graph.append([])
    for i in range(0, num_lines):
        graph[(tempG[i][0])].append([tempG[i][1], tempG[i][2]])

    return graph


# Calculate the number of nodes in a graph
def calcMax(n):
    dataFile = open(n, "r")
    num_lines = sum(1 for _ in open(n))
    largestNode = 0
    for i in range(0, num_lines):
        line = dataFile.readline().strip("\n")
        tokens = line.split(" ", 2)
        if largestNode < int(tokens[0]):
            largestNode = int(tokens[0])
        if largestNode < int(tokens[1]):
            largestNode = int(tokens[1])
    return largestNode


dijkstra(getG("data.txt"), 1)
