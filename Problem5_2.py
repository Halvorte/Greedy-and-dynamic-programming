'''
Problem 5. Knapsack
Use the weights, profits, and knapsack capacity from the P08 dataset to find the optimal packing in two ways:

1.  With the fractional knapsack problem
2.  With the binary (0/1) knapsack problem
'''

# recursive Function to calculate the best items to put in knapsack
def knapsack(weight, value, capacity):
    #def knapSack(W, wt, val):
    n = len(value)
    table = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weight[i - 1] <= j:
                table[i][j] = max(value[i - 1]
                                  + table[i - 1][j - weight[i - 1]], table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j]

    return table[n][capacity]


# Function to get the
def dynamic_knapsack(W, wt, val, n):
    # Creating a 2d array to solve
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # solving each square in the array
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Return the value of the last element in the 2d array.
    return K[n][W]


# Function to set up array
def set_array(n, capacity):
    arr = []
    for i in range(n):
        tmp = []
        for j in range(capacity):
            tmp.append(0)
        arr.append(tmp)
    return arr


def get_info():
    # Read weights from files
    file1 = open('dataKnapsack/p08_w.txt', 'r')
    weights_ = file1.readlines()
    file1.close()
    # Read profits from files
    file2 = open('dataKnapsack/p08_p.txt', 'r')
    value_ = file2.readlines()
    file2.close()
    # Read capacity from file
    file3 = open('dataKnapsack/p08_c.txt', 'r')
    capacity_ = file3.readline()
    file3.close()

    value = []
    weights = []

    for i in weights_:
        weights.append(int(i))

    for j in value_:
        value.append(int(i))

    capacity = int(capacity_)

    return capacity, weights, value


if __name__ == '__main__':
    # Binary knapsack problem

    #capacity, weight, value = get_info()
    #print(f'capacity: {capacity}')
    #print(f'weight: {weight}')
    #print(f'value: {value}')

    # capacity of sack
    capacity = 10

    # Items
    # nr of items
    weight = [1, 2 ,4 ,2, 5]
    # value of items
    value = [5, 3, 5, 3, 2]
    n = len(value)
    # weight of items



    # Initialize a 2d-array n*capacity
    #arr = set_array(n, capacity)


    ### Fix this function to use 2d array
    #answ = knapsack(weight, value, capacity)
    #print(answ)

    new_answ = dynamic_knapsack(capacity, weight, value, n)
    print(new_answ)
