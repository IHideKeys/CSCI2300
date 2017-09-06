from heapq import *


class Node(object):
    left = None
    right = None
    char = None
    frequency = 0

    def __init__(self, ch, f):
        self.char = ch
        self.frequency = f

    def setChildren(self, ln, rn):
        self.left = ln
        self.right = rn

    # Implement for PQ comparisons
    def __cmp__(self, a):
        return cmp(self.frequency, a.frequency)


def huffman(f):
    # Fill the queue with a node for each letter, frequency combination
    # Set the character of the node
    # Count the number of times the character occurs and set the frequency
    pq = []
    for key in f:
        n = Node(key, f[key])
        pq.append(n)

    # Create PQ
    heapify(pq)

    while len(pq) > 1:
        # Get left and right children
        l = heappop(pq)
        r = heappop(pq)
        # Create new node with frequency of the sum of children
        n = Node(None, r.frequency + l.frequency)
        n.setChildren(l, r)
        # Add the node to the heap
        heappush(pq, n)

    codes = {}

    # Start at root
    findEncoding("", pq[0], codes)

    return codes


def getFrequencies(n):
    freqs = {}
    # Open file
    # Count characters
    # Update dictionary as new characters are found
    with open(n) as f:
        for line in f:
            for ch in line:
                if freqs.__contains__(ch):
                    freqs[ch] += 1
                else:
                    freqs.update({ch: 1})
    return freqs


# Recursively walk the tree in order to get the encoding
def findEncoding(path, n, codes):
    # Check to see if there is a character or not associated with this node
    if n.char:
        # Update dictionary with the encoding
        codes[n.char] = path
    else:
        # Walk left
        findEncoding(path + "0", n.left, codes)
        # Walk right
        findEncoding(path + "1", n.right, codes)


# Encode the message using the code dictionary
def encodeMessage(code):
    encoding = ""
    length = 0
    with open(n) as f:
        for line in f:
            for ch in line:
                encoding += code[ch]
                length += len(code[ch])
    print("Length: " + str(length))
    return encoding


input = ""
n = "huffman.txt"
freqs = getFrequencies(n)
print(freqs)

print(huffman(freqs))
print(encodeMessage(huffman(freqs)))
