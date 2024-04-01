from Node import Node
from BSTChecker import check_bst_validity

# Get user input and parse into a binary tree
user_input = input()
user_root = Node.parse(user_input)
if user_root == None:
    print("Failed to parse input tree")
else:
    bad_node = check_bst_validity(user_root)
    if bad_node != None:
        print(str(bad_node.key))
    else:
        print("None")