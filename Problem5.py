'''
Problem 5. Knapsack
Use the weights, profits, and knapsack capacity from the P08 dataset to find the optimal packing in two ways:

1.  With the fractional knapsack problem
2.  With the binary (0/1) knapsack problem
'''


import random

# Function to create items for fractional knapsack

def items(nbr_of_items):

    items = []

    if nbr_of_items < 1:
        return

    for i in range(1, nbr_of_items):
        rand_value = random.randint(2, 20)
        rand_weight = random.randint(1, 10)
        dictionary = {
            'Item' : i,
            'Value' : rand_value,
            'Weight' : rand_weight,
            'V/W' : rand_value / rand_weight
        }
        items.append(dictionary)

    return items


def value_weight(items):
    for i in items:

        print(i)





if __name__ == '__main__':
    # Create random items with random value and weight. Also calculates value to weight ratio.
    items_list = items(20)

    # calculate the value to weight ratio of all the items
    value_weight(items_list)

