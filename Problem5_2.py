'''
Problem 5. Knapsack
Use the weights, profits, and knapsack capacity from the P08 dataset to find the optimal packing in two ways:

1.  With the fractional knapsack problem
2.  With the binary (0/1) knapsack problem
'''

# recursive Function to calculate the best items to put in knapsack
def knapsack(n, weight, value, capacity):
    if n == 0 or capacity == 0:
        return

    if weight[n-1] > capacity:
        return knapsack(n-1, weight, value, capacity)
    else:
        return max(value[n-1] + knapsack(n-1, weight, value, capacity - weight[n-1]),
                   knapsack(n-1, weight, value, capacity))


# Function to set up array
def set_array(n, capacity):
    arr = []
    for i in range(n):
        tmp = []
        for j in range(capacity):
            tmp.append(0)
        arr.append(tmp)
    return arr


if __name__ == '__main__':
    # Binary knapsack problem

    # capacity of sack
    capacity = 10

    # Items
    # nr of items
    n = 5
    # weight of items
    weight = [1, 2 ,4 ,2, 5]
    # value of items
    value = [5, 3, 5, 3, 2]


    # Initialize a 2d-array n*capacity
    arr = set_array(n, capacity)


    ### Fix this function to use 2d array
    answ = knapsack(n, weight, value, capacity)
    print(answ)
