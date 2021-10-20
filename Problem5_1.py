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


def sorted_VW(items):
    sorted_items = sorted(items, key=lambda x: x['V/W'], reverse=True)
    return sorted_items


# Function to choose items to put in the sack
def items_in_sack(items, sack_size):
    room_left = sack_size
    items_in_sack = []
    chosen_items = []

    for i in items:
        #print(f'Room left: {room_left}')
        #print(f"yo: {i['Weight']}")
        if i['Weight'] <= room_left:
            items_in_sack.append(i)
            room_left -= i['Weight']
            #print(f"yo: {i['Weight']}")
            chosen_items.append(f"{i}")
        elif i['Weight'] > room_left and room_left > 0:
            # add (room_left / weight) * weight
            fraction_of_item = (room_left/i['Weight']) * i['Weight']
            #print(f'Fraction: {fraction_of_item}')
            room_left -= fraction_of_item
            #print(f"yo: {i['Weight']}")
            chosen_items.append(f" {fraction_of_item}  of {i}")
        else:
            break

    # print(f'Items to pack: {items_in_sack}')
    print(f'Items: {chosen_items}')

    return chosen_items





if __name__ == '__main__':
    # Size of sack
    sack_size = 15

    # Create random items with random value and weight. Also calculates value to weight ratio.
    items_list = items(20)

    # Sort items after highest value to weight ratio
    sorted_items = sorted_VW(items_list)

    # Choose the items to add to the sack using fractional knapsack problem.
    chosen_items = items_in_sack(sorted_items, sack_size)

