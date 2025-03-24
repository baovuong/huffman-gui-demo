from queue import PriorityQueue

class Node:
    def __init__(self, weight, symbol=None):
        self.symbol = symbol
        self.weight = weight
        self.left = None
        self.right = None
        self.parent = None # Pointer to the parent node

    def __lt__(self, other):
        return self.weight < other.weight


def compress(value):

    # Count the frequency of each character
    frequency = {}
    for symbol in value:
        if symbol not in frequency:
            frequency[symbol] = 0
        frequency[symbol] += 1

    # Create a priority queue to store the nodes
    pq = PriorityQueue()
    for symbol, weight in frequency.items():
        pq.put((weight, Node(symbol, weight)))

    return 'compressed ' + value
     
def decompress(value):
    return 'uncompressed ' + value