'''
Problem 3. Huffman coding
In this assignment, you should make a lossless compressor using Huffman coding. Make an application that can take as input an arbitrary text consisting of the 29 Norwegian characters and compress the text using:

1.  Huffman coding with fixed-length encoding
2.  Huffman coding with variable size encoding The compressed text should include the characters (assume ASCII), codes, and the message.
'''
import itertools


# Function to give each letter a unique binary code
def set_fixed_encoding(alphabet):
    letters = []

    # Find the needed bit for each letters code
    count = 1
    while True:
        if len(alphabet) <= 2**count:
            #print(f'code will need to be {count} bits')
            break
        else:
            count += 1

    # List of each unique binary code given its power.
    lst = list(itertools.product([0, 1], repeat=count))

    # Cleaning up the binary codes
    joined = []
    for j in lst:
        string_ints = [str(int) for int in j]
        string_of_ints = ''.join(string_ints)

        joined.append(string_of_ints)

    # Create the dictionaries
    for i in range(len(alphabet)):
        dictionary = {
            'Letter': alphabet[i],
            'Fixed Code': joined[i]
        }
        letters.append(dictionary)

    # Return list of dictionaries containing letters and code
    return letters


# Function to convert a string to huffman code
def to_code(string, letters):
    code = []
    for i in string:
        for j in letters:
            if i == j['Letter']:
                code.append(j['Fixed Code'])

    return code


# Function to convert binary code to string
def to_string(binary, letters):
    strng = []
    to_translate = []
    n = 5

    for j in range(0, len(binary), n):
        to_translate.append(binary[j : j + n])
    print(to_translate)

    for i in to_translate:
        for k in letters:
            if i == k['Fixed Code']:
                strng.append(k['Letter'])

    return strng


if __name__ == '__main__':
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ'

    # function to create a fixed length code for each letter in the alphabet
    letters = set_fixed_encoding(string)

    print(letters)

    # Function to convert string to huffman code
    code = to_code('HALLO', letters)
    print(code)

    # convert binary code to string
    word = to_string('011110010010001', letters)
    print(word)


