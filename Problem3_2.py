'''
Problem 3. Huffman coding
In this assignment, you should make a lossless compressor using Huffman coding. Make an application that can take as input an arbitrary text consisting of the 29 Norwegian characters and compress the text using:

1.  Huffman coding with fixed-length encoding
2.  Huffman coding with variable size encoding The compressed text should include the characters (assume ASCII), codes, and the message.
'''

# Variable size encoding

# Class for tree node
import queue
class Node:

    def __init__(self, letter, freq):
        self.letter = letter
        self.freq = freq
        self.left = None
        self.right = None
        self.direction = ''

    def setLeftChild(self, left):
        self.left = left

    def setRightChild(self, right):
        self.right = right



# Function to build the Huffman tree
def huffman_tree(sorted_symbols):
    nodes = []
    print(f'sorted symbs: {sorted_symbols}')
    # Create all the nodes
    for i in sorted_symbols:
        node = Node(i[0], i[1])
        nodes.append(node)

    #print("nodes")
    #for j in nodes:
    #    print(j.letter)

    # Sort the nodes in ascending order and ..
    while len(nodes) > 1:
        #nodes = sorted(nodes, key=lambda x: x.freq)

        # Take the smallest two nodes in node
        left = nodes[0]
        right = nodes[1]

        # Give the nodes direction value
        left.direction = 0
        right.direction = 1

        newNodeLetter = str(left.letter) + str(right.letter)
        newNodeFreq = left.freq + right.freq
        #print(f'newNodeFreq: {newNodeFreq}')
        new_node = Node(newNodeLetter, newNodeFreq)
        new_node.setLeftChild(left)
        new_node.setRightChild(right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    return nodes[0]


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
def print_tree(node): #, #val=''):
    # Get the huffman code
    #newVal = val + node.direction

    print(f'Visiting: {node.letter} with value: {node.freq} huffman code: {node.direction}')

    # If node is not an edge node, traverse it.
    if (node.left):
        #print_tree(node.left, newVal)
        print_tree(node.left)
    if (node.right):
        #print_tree(node.right, newVal)
        print_tree(node.right)

    # If node is edge node
    if (not node.left and node.right):
        print('edge:')
        print(f'{node.letter} | {node.freq} | {newVal}')


# Function to find path from every end node to root. Then find huffman code for each letter.
def find_path(node, sorted_symbols):
    arr = []

    for i in sorted_symbols:

        # Run funciton to find the path from root to i/given node

        if has_path(node, arr, i[0]):
            for j in range(len(arr) - 1):
                print(arr[j], end="->")
            print(arr[len(arr) - 1])

        else:
            print("No Path")



def has_path(root, arr, x):

    if root is None:
        return False

    arr.append(root.direction)

    if root.letter == x:
        return True

    if has_path(root.left, arr, x) or has_path(root.right, arr, x):
        return True



if __name__ == '__main__':
    # String consisting of all the letters in the norwegian alphabet
    encoding_string = 'AAAAAAAAAAAABBBBBBBCCCDDDDDDDDDDDDDDEEEEEEEEEEEEEEEEEEEEEEEEEEEEFFFFFFFFFGGGGGHHHHHHHHHHHHHHHHHHHHHHIIIIIIIIJJJJJKKKKLLLMMMMNNNNNOOOPPQRRRRRRRRRSSSSSSTTTTTTUUUUVVVWWWWXXXXYYYZZZÆÆØÆÆÆÆØØØØØØØØØØØØØØØØÅÅÅÅÅÅÅÅÅÅ'

    # Sorting the letters in descending order after count of each letter
    sorted_symbols = probablity(encoding_string)

    # Create the Huffman tree
    treeRoot = huffman_tree(sorted_symbols)

    find_path(treeRoot, sorted_symbols)

    # Print the tree given the root node
    print_tree(treeRoot)

