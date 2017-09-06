import heapdict


def dijkstra(G, E, s, t):
    dist = [float('inf') for _ in range(len(G))]
    prev = [None for _ in range(len(G))]
    dist[s] = 0
    hd = heapdict.heapdict()
    for i in range(0, len(G)):
        hd[i] = dist[i]

    while len(hd) != 0:
        u = hd.popitem()[0]
        for i in range(0, len(G[u])):
            v = G[u][i]
            if E.get((u, v)) is not None and float(dist[v]) > float(dist[u] + E.get((u, v))):
                dist[v] = float(dist[u] + E.get((u, v)))
                prev[v] = int(u)
                hd.__setitem__(v, dist[v])
    path = []
    i = len(prev) - 1
    if i == t:
        if prev[i] is not None:
            j = prev[i]
            path.insert(0, i)
            path.insert(0, j)
            while j != s:
                j = prev[j]
                path.insert(0, j)
        elif prev[i] is None and i == s:
            path.append(i)

    return path, dist


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
    largestNode = calcMaxMin(n)
    for i in range(0, largestNode[0]):
        graph.append([])
    for i in range(0, num_lines):
        if tempG[i][1] and tempG[i][2]:
            graph[(tempG[i][0])].append(tempG[i][1])

    return graph


def createEdgeDict(n):
    dataFile = open(n, "r")
    num_lines = sum(1 for _ in open(n))
    edgeDict = {}
    for i in range(0, num_lines):
        line = dataFile.readline().strip("\n")
        tokens = line.split(" ", 2)
        line.split(" ", num_lines)
        if len(tokens) > 1:
            edgeDict.update({(int(tokens[0]), int(tokens[1])): int(tokens[2])})

    return edgeDict


# Calculate the number of nodes in a graph
def calcMaxMin(n):
    dataFile = open(n, "r")
    num_lines = sum(1 for _ in open(n))
    largestNode = 0
    minNode = num_lines
    for i in range(0, num_lines):
        line = dataFile.readline().strip("\n")
        tokens = line.split(" ", 2)
        if largestNode < int(tokens[0]):
            largestNode = int(tokens[0])
        if largestNode < int(tokens[1]):
            largestNode = int(tokens[1])
        if minNode > int(tokens[0]):
            minNode = int(tokens[0])
        if minNode > int(tokens[1]):
            minNode = int(tokens[1])
    return largestNode, minNode


def fordFulkerson(G, E, s, t):
    maxFlow = 0
    residual = getG("testlab9.txt")
    residualEdges = createEdgeDict("testlab9.txt")
    minOnPath = float('Inf')

    path = dijkstra(residual, residualEdges, s, t)[0]
    while len(path) != 0:
        path = dijkstra(residual, residualEdges, s, t)[0]
        for i in range(0, len(path) - 1):
            if residualEdges.get((path[i], path[i + 1])) < minOnPath:
                minOnPath = residualEdges.get((path[i], path[i + 1]))
        if len(path) > 0:
            maxFlow += minOnPath

        for j in range(0, len(path) - 1):
            residualEdges.update({(path[j], path[j + 1]): residualEdges.get((path[j], path[j + 1])) - minOnPath})
            residualEdges.update({(path[j + 1], path[j]): minOnPath})

            list_does_contain = next((True for item in residual[path[j + 1]] if item == path[j]), False)
            if not list_does_contain:
                residual[path[j + 1]].append(path[j])

            for i in range(0, len(residual)):
                for j in range(0, len(residual[i])):
                    if len(residual[i]) > j and residualEdges.get((i, residual[i][j])) == 0:
                        residualEdges.update({(i, residual[i][j]): float('inf')})
                        residual[i].remove(residual[i][j])

        dist1 = dijkstra(residual, E, s, t)[1]

        scut = []
        tcut = []
        for i in range(0, len(dist1)):
            if dist1[i] != float('inf'):
                scut.append(i)
            else:
                tcut.append(i)
    print("Set S: " + str(scut))
    print("Set V-S: " + str(tcut))
    print("MIN-CUT Edge Weights")
    edges = createEdgeDict("testlab9.txt")
    sum = 0
    for j in range(0, len(scut)):
        for i in range(0, len(G)):
            if residualEdges.get((i, scut[j])) < float('inf'):
                if residualEdges.get((i, scut[j])) is not None and not scut.__contains__(i):
                    print("(" + str(i) + "," + " " + str(scut[j]) + ")" + " : " + str(edges.get((scut[j], i))))
                    sum += edges.get((scut[j], i))
    print("SUM: " + str(sum))
    print(residualEdges)
    return maxFlow


maxMinTuple = calcMaxMin("testlab9.txt")
s = maxMinTuple[1]
t = maxMinTuple[0]

print("MAX FLOW: " + str(fordFulkerson(getG("testlab9.txt"), createEdgeDict("testlab9.txt"), s, t)))
