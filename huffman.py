from queue import PriorityQueue

class Node:
    def __init__(self, weight, symbol=None):
        self.symbol = symbol
        self.weight = weight
        self.left = None
        self.right = None
        self.parent = None # Pointer to the parent node

    def is_leaf(self):
        return self.left is None and self.right is None
    
    def set_left(self, node):
        self.left = node
        node.parent = self

    def set_right(self, node):
        self.right = node
        node.parent = self
    
    def __str__(self):
        return f"{self.symbol}({self.weight})"
    
    __repr__ = __str__

    def __lt__(self, other):
        return self.weight < other.weight
    

def to_bin(value):
    return ''.join([format(ord(x), '08b') for x in value])

def max_bitsize(value):
    return max([(ord(x)-32).bit_length() for x in value])

"""create binary tree
Create a binary tree from a priority queue of nodes
returns the root node of the tree
""" 
def create_binary_tree(node_queue):
    while node_queue.qsize() > 1:
        node1 = node_queue.get()[1]
        node2 = node_queue.get()[1]
        
        new_node = Node(node1.weight + node2.weight)
        new_node.set_left(node1)
        new_node.set_right(node2)
        node_queue.put((new_node.weight, new_node))
    
    return node_queue.get()[1]

def create_codes(node, code='', codes={}):
    if node.is_leaf():
        codes[node.symbol] = code
    else:
        create_codes(node.left, code + '0', codes)
        create_codes(node.right, code + '1', codes)
    return codes

def encode_tree(node, bitsize=8):
    if node.is_leaf():
        return '1' + node.symbol + ' ' # format(ord(node.symbol), '0%xb' % bitsize)
    else:
        return '0 ' + encode_tree(node.left, bitsize) + encode_tree(node.right, bitsize)


"""
function to compress a string using huffman encoding
format: <char bitsize(4)><tree(variable)><encoded value(variable)>
"""
def compress(value):

    print('before: %s' % to_bin(value))

    # Count the frequency of each character
    frequency = {}
    for symbol in value:
        if symbol not in frequency:
            frequency[symbol] = 0
        frequency[symbol] += 1

    # Create a priority queue to store the nodes
    pq = PriorityQueue()
    for symbol, weight in frequency.items():
        pq.put((weight, Node(weight, symbol)))

    # Build the Huffman tree
    root = create_binary_tree(pq)

    # Traverse the tree to get the codes
    codes = create_codes(root)

    # Encode tree
    bits = max_bitsize(value)
    print(bits)
    encoded_tree = encode_tree(root, bits)

    # Encode the value
    encoded_value = ' '.join([codes[symbol] for symbol in value])

    output = format(bits, '04b') + ' ' + encoded_tree + encoded_value
    print(output)
    
    #return ('%x' % int(output, 2)).decode('hex').decode('utf-8')
    return output
     
def decompress(value):

    # Decode the tree

    # Decode the value
    return 'uncompressed ' + value