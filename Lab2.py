import random
import time


# Get bit-length of an integer
def bit_length(x):
    str = bin(x)
    str = str.lstrip('-0b')
    return len(str)


# Generate a random d-digit integer
def genRand(d):
    rand = random.randint(10 ** (d - 1), (10 ** d) - 1)
    return rand


# Method 1
# Implementation of the grade school method
# of multiplication using bit-shifts only.

# noinspection PyShadowingNames
def gradeSchoolMult(x, y):
    # type: (int, int) -> int
    sum = 0
    i = 0
    # Base case
    if y == 0:
        return 0

    else:
        while y > 0:
            temp = y
            y >>= 1
            # Check to see if the current bit is a 1 or a 0
            if y << 1 != temp:
                # Add to the sum, x shifted by i bits if the current bit of y is on
                sum += x << i
            i += 1

    return sum


# Method 2
# Implementation of fig 1.1

def multiply(x, y):
    # Base Case
    if y == 0:
        return 0

    z = multiply(x, y >> 1)

    temp = y
    y >>= 1
    if y << 1 == temp:
        return z << 1
    else:
        return x + (z << 1)


# Method 3
# Implementation of divide and conquer approach

# noinspection PyShadowingNames
def divAndConquerMult(x, y):
    x_bit_len = bit_length(x)
    y_bit_len = bit_length(y)

    if x_bit_len > y_bit_len:
        n = x_bit_len
    else:
        n = y_bit_len

    if y == 0 or x == 0:
        return 0

    if x_bit_len == 1 or y_bit_len == 1:
        if x_bit_len == 1:
            return y
        else:
            return x

    m = n >> 1

    x_l = x >> m
    mask_x = (1 << m) - 1
    x_r = x & mask_x

    mask_y = (1 << m) - 1
    y_l = y >> m
    y_r = y & mask_y

    p_1 = divAndConquerMult(x_l, y_l)
    p_2 = divAndConquerMult(x_r, y_r)
    p_3 = divAndConquerMult((x_l + x_r), (y_l + y_r))

    return (p_1 << ((n >> 1) << 1)) + ((p_3 - p_1 - p_2) << (n >> 1)) + p_2


x = genRand(100000)
y = genRand(100000)

start = time.time()
print("Method One")
print("x,y: " + str(x) + ", " + str(y))
print("Product: " + str(gradeSchoolMult(x, y)))
print("Time: " + str(time.time() - start) + "\n")

#start = time.time()
#print("Method Two")
#print("x,y: " + str(x) + ", " + str(y))
#print("Product: " + str(multiply(x, y)))
#print("Time: " + str(time.time() - start) + "\n")

start = time.time()
print("Method Three")
print("x,y: " + str(x) + ", " + str(y))
print("Product: " + str(divAndConquerMult(x, y)))
print("Time: " + str(time.time() - start) + "\n")
