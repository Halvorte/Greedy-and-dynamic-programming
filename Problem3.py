'''
Problem 3. Huffman coding
In this assignment, you should make a lossless compressor using Huffman coding. Make an application that can take as input an arbitrary text consisting of the 29 Norwegian characters and compress the text using:

1.  Huffman coding with fixed-length encoding
2.  Huffman coding with variable size encoding The compressed text should include the characters (assume ASCII), codes, and the message.
'''

# Class for tree node
import queue


class Node:

    def __init__(self, letter, freq, left=None, right=None):
        self.letter = letter
        self.freq = freq
        self.left = left
        self.right = right
        self.direction = ''
'''
    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)
'''

# Function to build the Huffman tree
def huffman_tree(sorted_symbols):
    nodes = []
    # Create all the nodes
    for i in sorted_symbols:
        nodes.append(Node(i[0], i[1]))

    print(nodes)
    # Sort the nodes in ascending order and ..
    while len(nodes) > 1:
        #nodes = sorted(nodes, key=lambda x: x.freq)

        left = nodes[0]
        right = nodes[1]

        left.direction = 0
        right.direction = 1

        new_node = Node((str(left.letter) + str(right.letter)), (int(left.freq) + int(right.freq)), left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)
        print("ha")

    return nodes


# Function to get the different letters and how many times they appear in the encoding string and sort them.
def probablity(string):
    symbols = {}
    for i in string:
        if i not in symbols:
            symbols[i] = 1
        else:
            symbols[i] += 1

    # Sorting the symbols dictionary
    sorted_sym = sorted(symbols.items(), key=lambda x: x[1], reverse=False)
    print(sorted_sym)
    return sorted_sym


# Funciton to print node-tree
def print_tree(node, val=''):
    # Get the huffman code
    newval = val + node.direction

    # If node is not an edge node, traverse it.
    if (node.left):
        print_tree(node.left, newval)
    if (node.right):
        print_tree(node.right, newval)

    # If node is edge node
    if (not node.left and node.right):
        print(f'{node.letter} | {node.freq} | {newval}')



if __name__ == '__main__':
    # String consisting of all the letters in the norwegian alphabet
    encoding_string = 'AAAAAAAAAAAABBBBBBBCCCDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFGGGGGHHHHHHHHHHHHHHHHHHHHHHIIIIIIIIJJJJJKKKKLLLMMMMNNNNNOOOPPQRRRRRRRRRSSSSSSTTTTTTUUUUVVVWWWWXXXXYYYZZZÆÆØÆÆÆÆØØØØØØØØØØØØØØØØÅÅÅÅÅÅÅÅÅÅ'

    # Sorting the letters in descending order after count of each letter
    sorted_symbols = probablity(encoding_string)

    # Create the Huffman tree
    tree = huffman_tree(sorted_symbols)

    # Print the tree
    print_tree(tree)

