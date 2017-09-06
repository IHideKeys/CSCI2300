# globals
visited = []
post = []
pre = []
ccnum = []
clock = 1
cc = 0
processOrder = []
SCC = [[]]


# Calculate the number of nodes in a graph
def calcMax(n):
    dataFile = open(n, "r")
    num_lines = sum(1 for _ in open(n))
    largestNode = 0
    for i in range(0, num_lines):
        line = dataFile.readline().strip("\n")
        tokens = line.split(" ", 2)
        line.split(" ", num_lines)
        if largestNode < tokens[0]:
            largestNode = int(tokens[0])
        if largestNode < int(tokens[1]):
            largestNode = int(tokens[1])

    return largestNode


# Create reverse graph
def reverseG(n):
    dataFile = open(n, "r")
    num_lines = sum(1 for _ in open(n))
    tempGReverse = [[0 for _ in range(2)] for _ in range(num_lines)]
    gReverse = [[]]
    for i in range(0, num_lines):
        line = dataFile.readline().strip("\n")
        tokens = line.split(" ", 2)
        line.split(" ", num_lines)
        if len(tokens) > 1:
            temp = int(tokens[0])
            tokens[0] = int(tokens[1])
            tokens[1] = temp
            for j in range(0, 2):
                tempGReverse[i][j] = tokens[j]

    largestNode = calcMax(n)
    for i in range(0, largestNode - 1):
        gReverse.append([])
    for i in range(0, num_lines):
        gReverse[(tempGReverse[i][0] - 1)].append(tempGReverse[i][1])

    return gReverse


def getG(n):
    dataFile = open(n, "r")
    num_lines = sum(1 for _ in open(n))
    tempG = [[0 for _ in range(2)] for _ in range(num_lines)]
    graph = [[]]
    for i in range(0, num_lines):
        line = dataFile.readline().strip("\n")
        tokens = line.split(" ", 1)
        line.split(" ", num_lines)
        if len(tokens) > 1:
            for j in range(0, 2):
                tempG[i][j] = int(tokens[j])

    largestNode = calcMax(n)
    for i in range(0, largestNode - 1):
        graph.append([])
    for i in range(0, num_lines):
        graph[(tempG[i][0] - 1)].append(tempG[i][1])

    return graph


def explore(G, v):
    global visited
    visited[v] = True
    preVisit(v)
    for i in range(0, len(G[v])):
        u = G[v][i]
        if not visited[u - 1]:
            explore(G, u - 1)
    postVisit(v)


def explore2(G, v):
    global visited
    global SCC
    global cc
    visited[v] = True
    preVisit2(v)
    for i in range(0, len(G[v])):
        u = G[v][i]
        if not visited[u - 1]:
            explore2(G, u - 1)
    postVisit2(v)


def dfs(G):
    global visited
    global cc
    global ccnum
    for i in range(0, len(G)):
        visited.append(False)
        post.append(None)
        ccnum.append(None)
        pre.append(None)
    for i in range(0, len(G)):
        if not visited[i]:
            explore(G, i)
            cc += 1


def dfs2(G):
    global visited
    global cc
    global ccnum
    global SCC
    global processOrder
    i = len(G)
    cc = 0
    ccnum = [None for _ in range(0, len(G))]
    visited = [False for _ in range(0, len(G))]
    for i in range(0, len(G)):
        visited.append(False)
        post.append(None)
        pre.append(None)
    while i >= 0:
        v = processOrder[i]
        if not visited[v]:
            SCC.append([])
            explore2(G, v)
            cc += 1
        i -= 1


def preVisit(v):
    global clock
    global pre
    global ccnum
    global cc
    pre[v] = clock
    clock += 1
    ccnum[v] = cc


def preVisit2(v):
    global clock
    global pre
    global ccnum
    global cc
    global SCC
    pre[v] = clock
    clock += 1
    ccnum[v] = cc
    SCC[cc].append(v + 1)


def postVisit2(v):
    global clock
    global post
    post[v] = clock
    clock += 1


def postVisit(v):
    global clock
    global post
    global processOrder
    post[v] = clock
    clock += 1
    processOrder.append(v)

n = raw_input("Enter file name: ")
reversedGraph = reverseG(n)
dfs(reversedGraph)

graph = getG(n)
dfs2(graph)

for i in range(1, len(SCC)):
    print("SCC " + str(i) + ": " + str(SCC[i - 1]))
