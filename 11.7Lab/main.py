from Searcher import Searcher
from NumComparer import NumComparer
from StringComparer import StringComparer

def main():
    sorted_fruits = [
        "Apple", "Apricot", "Banana", "Blueberry", "Cherry",
        "Grape", "Grapefruit", "Guava", "Lemon", "Lime", "Orange",
        "Peach", "Pear", "Pineapple", "Raspberry", "Strawberry"
    ]
    fruit_searches = [
        "Nectarine", "Mango", "Guava", "Strawberry",
        "Kiwi", "Apple", "Raspberry", "Carrot", "Lemon", "Bread"
        ]
    expected_fruit_search_results = [-1, -1, 7, 15, -1, 0, 14, -1, 8, -1]

    string_comparer = StringComparer()
    print_searches(sorted_fruits,
                   fruit_searches,
                   string_comparer,
                   expected_fruit_search_results,
                   True)

    # Perform sample searches with integers
    integers = [11, 21, 27, 34, 42, 58, 66, 71, 72, 85, 88, 91, 98]
    integer_searches = [42, 23, 11, 19, 87, 98, 54, 66, 92, 1, 14, 21, 66, 87, 83]
    expected_integer_search_results = [4, -1, 0, -1, -1, 12, -1, 6, -1, -1, -1, 1, 6, -1, -1]

    num_comparer = NumComparer()
    print_searches(integers,
                   integer_searches,
                   num_comparer,
                   expected_integer_search_results,
                   False)

def print_searches(sorted_list,
                   search_keys,
                   comparer,
                   expected_results,
                   key_in_quotes):
    # If key_in_quotes is True, " characters surround the key in output
    # statements. Otherwise empty strings surround the key.
    extra = '\"' if key_in_quotes else ''

    for i in range(len(search_keys)):
        # Get the key to search for
        search_key = search_keys[i]

        # Peform the search
        index = Searcher.binary_search(sorted_list, search_key, comparer)

        # Compare actual result against expceted
        expected = expected_results[i]
        if index == expected:
            print(f"PASS: Search for key {extra}{search_key}{extra} returned {expected}.")
        else:
            print(f"FAIL: Search for key {extra}{search_key}{extra} should have returned {expected}, but returned {index}.")

if __name__ == '__main__':
    main()
