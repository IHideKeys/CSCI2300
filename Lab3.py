import math
import random


def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, int(math.floor(y / 2)), N)
    if y % 2 == 0:
        return (z * z) % N
    else:
        return x * ((z * z) % N)


def primality(N, k):
    rand = []
    isPrime = False
    for x in range(0, k):
        rand.append(0)
    for y in range(0, k):
        rand[y] = random.randint(1, N - 1)
    for i in range(0, len(rand)):
        if modexp(rand[i], N - 1, N) == 1:
            isPrime = True
        else:
            return False
    return isPrime


def primalitycar(N, k):
    rand = []
    yes = 0
    for x in range(0, k):
        rand.append(0)
    for y in range(0, k):
        rand[y] = random.randint(1, N - 1)
    for i in range(0, len(rand)):
        if modexp(rand[i], N - 1, N) == 1:
            yes += 1

    return yes

carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973, 75361,
              101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561, 399001,
              410041, 449065, 488881]
num = 12341327
print("Primality of " + str(num) + " is: " + str(primality(num, 1000)))

for i in range(0, len(carmichael)):
    print(
        "Probability of " + str(carmichael[i]) + " is: " + str(float(primalitycar(carmichael[i], 1000)) / float(1000)) +
        "%")
