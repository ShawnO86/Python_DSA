#8.2.2
""" def find(lst, item, low, high, spacer):
    ''' Finds index of string in list of strings, else -1.
    Searches only the index range low to high
    Note: Upper/Lower case characters matter
    '''
    range_size = (high - low) + 1
    mid = (high + low) // 2

    if item == lst[mid]:  # Base case 1: Found at mid
        pos = mid
    elif range_size == 1:  # Base case 2: Not found
        pos = -1
    else:  # Recursive search: Search lower or upper half
        if item < lst[mid]:  # Search lower half
            print(f'{spacer}Low Find ({low}, {mid})')
            pos = find(lst, item, low, mid, spacer + '  ')
        else:  # Search upper half
            print(f'{spacer}High Find ({mid+1}, {high})')
            pos = find(lst, item, mid+1, high, spacer + '  ')

    return pos

alph = ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
pos = find(alph, 'C', 0, len(alph) - 1, '  ')

if pos >= 0:
    print(f'Found at position {pos}.')
else:
    print('Not found.') """

#8.5.1
""" def compute_nth_fib(n, spacer):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(spacer + '  ', n-1, n-2)
        return compute_nth_fib(n-1, spacer + 'f  ') + compute_nth_fib(n-2, spacer + 'l  ')
    
    
user_in = int(input())
print(compute_nth_fib(user_in, '  ')) """

#8.6.2
""" max_items_in_bag = 3

def shopping_bag_combinations(curr_bag, remaining_items, spacer = '  '):
    '''
    Output every combination of items that fit
    in a shopping bag. Each recursive call moves
    one item into the shopping bag.
    '''
    if len(curr_bag) == max_items_in_bag:
        # Base case: Shopping bag full
        bag_value = 0
        for item in curr_bag:
            bag_value += item['price']
            print(f'{item["name"]}  ', end=' ')
        print(f'= {bag_value}')
    else:
        # Recursive case: Move one of the remaining items
        # to the shopping bag.
        for index, item in enumerate(remaining_items):
            # Move item into bag
            curr_bag.append(item)
            remaining_items.pop(index)
            print(f'{spacer} Current bag: {curr_bag}')
            print(f'{spacer} Remaining: {remaining_items}')
            shopping_bag_combinations(curr_bag, remaining_items, spacer + '  ')

            # Take item out of bag
            print(f'Item out: {index} {item}')
            remaining_items.insert(index, item)
            curr_bag.pop()

items = [
    {
        'name': 'Milk',
        'price': 1.25
    },
    {
        'name': 'Belt',
        'price': 23.55
    },
    {
        'name': 'Toys',
        'price': 19.05
    },
    {
        'name': 'Cups',
        'price': 11.85
    }
]

bag = []
shopping_bag_combinations(bag, items) """