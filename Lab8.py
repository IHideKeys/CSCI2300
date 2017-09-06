# Created by Sajiel

def editDistance(s1, s2):
    m = len(s1)
    n = len(s2)
    # Hold edit distance values for each possible substring
    edit = [[None for _ in range(0, n+1)] for _ in range(0, m+1)]
    # Hold previous direction
    prev = [[None for _ in range(0, n+1)] for _ in range(0, m+1)]
    # Initial conditions
    for i in range(0, m+1):
        edit[i][0] = i
    for j in range(0, n+1):
        edit[0][j] = j
    # End initial conditions

    # Main loop
    for i in range(1, m+1):
        for j in range(1, n+1):
            diff = 1
            if s1[i-1] == s2[j-1]:
                diff = 0
            nextEdit = minEdit(edit[i - 1][j] + 1, edit[i][j - 1] + 1, edit[i - 1][j - 1] + diff)
            edit[i][j] = nextEdit[0]
            if nextEdit[1] == 0:
                prev[i][j] = "UP"
            elif nextEdit[1] == 1:
                prev[i][j] = "LEFT"
            elif nextEdit[1] == 2:
                prev[i][j] = "DIAG"

    alignmentS1 = ""
    alignmentS2 = ""
    i = m
    j = n
    prevDirection = prev[i][j]
    while prevDirection is not None:
        prevDirection = prev[i][j]
        if prevDirection == "UP":
            alignmentS1 += s1[i-1]
            alignmentS2 += "_"
            i -= 1
        elif prevDirection == "LEFT":
            alignmentS1 += "_"
            alignmentS2 += s2[j-1]
            j -= 1
        elif prevDirection == "DIAG":
            alignmentS1 += s1[i-1]
            alignmentS2 += s2[j-1]
            i -= 1
            j -= 1

    # Handle end conditions where one string is shorter than the other
    if m < n:
        i = n-m
        while i >= 0:
            alignmentS2 += s2[i]
            alignmentS1 += "_"
            i -= 1
    if n < m:
        i = m-n
        while i >= 0:
            alignmentS1 += s1[i]
            alignmentS2 += "_"
            i -= 1
    print(alignmentS1[::-1])
    print(alignmentS2[::-1])
    print("Edit Distance: " + str(edit[m][n]))


def minEdit(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        previousDirection = 0
        nextEdit = n1
    elif n2 < n1 and n2 < n3:
        previousDirection = 1
        nextEdit = n2
    else:
        previousDirection = 2
        nextEdit = n3
    return nextEdit, previousDirection

X = 'CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG'
Y = 'CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA'

editDistance(X, Y)
