'''
Problem 5. Knapsack
Use the weights, profits, and knapsack capacity from the P08 dataset to find the optimal packing in two ways:

1.  With the fractional knapsack problem
2.  With the binary (0/1) knapsack problem
'''


# Function to create items for fractional knapsack
def items(nbr_of_items):
    # Read weights from files
    file1 = open('dataKnapsack/p08_w.txt', 'r')
    weights = file1.readlines()
    file1.close()
    # Read profits from files
    file2 = open('dataKnapsack/p08_p.txt', 'r')
    profits = file2.readlines()
    file2.close()

    items = []

    if nbr_of_items < 1:
        return

    for i in range(nbr_of_items):
        value = int(profits[i])
        weight = int(weights[i])

        dictionary = {
            'Item' : i + 1,
            'Value' : value,
            'Weight' : weight,
            'V/W' : value / weight
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
    profit = 0

    for i in items:
        #print(f'Room left: {room_left}')
        #print(f"yo: {i['Weight']}")
        if i['Weight'] <= room_left:
            items_in_sack.append(i)
            room_left -= i['Weight']
            #print(f"yo: {i['Weight']}")
            chosen_items.append(f"{i}")
            profit += i['Value']
        elif i['Weight'] > room_left and room_left > 0:
            # add (room_left / weight) * weight
            fraction_of_item = (room_left/i['Weight']) * i['Weight']
            #print(f'Fraction: {fraction_of_item}')
            room_left -= fraction_of_item
            #print(f"yo: {i['Weight']}")
            chosen_items.append(f" {fraction_of_item}  of {i}")
            profit += (i['Value'] / i['Weight']) * fraction_of_item
        else:
            break

    # print(f'Items to pack: {items_in_sack}')
    print(f'Items: {chosen_items}')
    print(f'Profit: {profit}')

    return chosen_items





if __name__ == '__main__':
    # Size of sack
    file3 = open('dataKnapsack/p08_p.txt', 'r')
    capacity = file3.readline()
    file3.close()
    sack_size = int(capacity)

    # Create dictionaries for each item. Also calculates value to weight ratio.
    items_list = items(24)

    # Sort items after highest value to weight ratio
    sorted_items = sorted_VW(items_list)

    # Choose the items to add to the sack using fractional knapsack problem.
    chosen_items = items_in_sack(sorted_items, sack_size)

    # Print the chosen items and value


