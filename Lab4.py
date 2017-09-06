import random

import numpy
import time


# Basic n^3 matrix multiplication algorithm
def basic_matrix(X, Y):
    A = [[0 for _ in range(len(X))] for _ in range(len(X[0]))]

    # Rows
    for i in range(0, len(X)):
        # Columns
        for j in range(0, len(X[0])):
            for k in range(0, len(Y[0])):
                A[i][j] += X[i][k] * Y[k][j]

    return numpy.array(A)


def strassenMult(X, Y):
    size = len(X) // 2

    if len(X) == 1:
        return basic_matrix(X, Y)

    A = [[0 for _ in range(size)] for _ in range(size)]
    B = [[0 for _ in range(size)] for _ in range(size)]
    C = [[0 for _ in range(size)] for _ in range(size)]
    D = [[0 for _ in range(size)] for _ in range(size)]

    E = [[0 for _ in range(size)] for _ in range(size)]
    F = [[0 for _ in range(size)] for _ in range(size)]
    G = [[0 for _ in range(size)] for _ in range(size)]
    H = [[0 for _ in range(size)] for _ in range(size)]

    # Make the n/2 x n/2 sub matrices
    for i in range(size):
        for j in range(size):
            A[i][j] = X[i][j]
            B[i][j] = X[i][j + size]
            C[i][j] = X[i + size][j]
            D[i][j] = X[i + size][j + size]

            E[i][j] = Y[i][j]
            F[i][j] = Y[i][j + size]
            G[i][j] = Y[i + size][j]
            H[i][j] = Y[i + size][j + size]

    # Calculate P1...P7
    P1 = strassenMult(A, subMatrix(F, H))
    P2 = strassenMult(addMatrix(A, B), H)
    P3 = strassenMult(addMatrix(C, D), E)
    P4 = strassenMult(D, subMatrix(G, E))
    P5 = strassenMult(addMatrix(A, D), addMatrix(E, H))
    P6 = strassenMult(subMatrix(B, D), addMatrix(G, H))
    P7 = strassenMult(subMatrix(A, C), addMatrix(E, F))

    # Calculate sub-matrices of the product matrix
    P11 = addMatrix(subMatrix(addMatrix(P5, P4), P2), P6)
    P12 = addMatrix(P1, P2)
    P21 = addMatrix(P3, P4)
    P22 = subMatrix(subMatrix(addMatrix(P1, P5), P3), P7)

    P = [[0 for _ in range(len(X))] for _ in range(len(X))]

    # Create product matrix using the sub-matrices
    for i in range(size):
        for j in range(size):
            P[i][j] = P11[i][j]
            P[i][size + j] = P12[i][j]
            P[i + size][j] = P21[i][j]
            P[i + size][j + size] = P22[i][j]

    return numpy.array(P)


def addMatrix(X, Y):
    A = [[0 for _ in range(len(X))] for _ in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X)):
            # Add corresponding elements in each matrix
            A[i][j] = X[i][j] + Y[i][j]
    return A


def subMatrix(X, Y):
    A = [[0 for _ in range(len(X))] for _ in range(len(X[0]))]
    for i in range(len(X)):
        for j in range(len(X)):
            # Add corresponding elements in each matrix
            A[i][j] = X[i][j] - Y[i][j]
    return A


n = 1024
X = numpy.random.rand(n, n)
Y = numpy.random.rand(n, n)
# print(X)
# print(Y)
start = time.time()
numpy.dot(X, Y)
print ("Numpy: " + str(time.time() - start))

start = time.time()
basic_matrix(X, Y)
print ("Basic matrix run time: " + str(time.time() - start))

start = time.time()
strassenMult(X, Y)
print ("Strassen matrix run time: " + str(time.time() - start))

# print(numpy.dot(X, Y))
