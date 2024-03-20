from SortedNumberList import SortedNumberList

def main():
    # Read the line of input numbers
    terms = input().split()
    print('first terms:', terms)
    sorted_list = SortedNumberList()
    # Insert each value and show the sorted list's contents after each insertion
    for term in terms:
        number = float(term)
        print(f"""List after inserting {number}: """)
        sorted_list.insert(number)
        print_list(sorted_list)

    # Uncomment the block below for Step 4

    # Read the input line with numbers to remove
    terms = input().split()
    print('second terms:', terms)
    for term in terms:
        number = float(term)
        print(f"""List after removing {number}: """)
        sorted_list.remove(number)
        print_list(sorted_list)


# Prints the sorted_number_list's contents, in order from head to tail
def print_list(lst):
    node = lst.head
    while node != None:
        print(node.get_data(), end=' ',)
        node = node.get_next()
    print()

if __name__ == '__main__':
    main()