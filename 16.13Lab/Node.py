class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        
    # Counts the number of nodes in this tree
    def count(self):
        left_count = 0
        if self.left != None:
            left_count = self.left.count()
        right_count = 0
        if self.right != None:
            right_count = self.right.count()
        return 1 + left_count + right_count
    
    # Inserts the new node into the tree.
    def insert(self, node):
        current_node = self
        while current_node is not None: 
            if node.key < current_node.key:
                # If there is no left child, add the new
                # node here; otherwise repeat from the
                # left child.
                if current_node.left is None:
                    current_node.left = node
                    current_node = None
                else:
                    current_node = current_node.left
            else:
                # If there is no right child, add the new
                # node here; otherwise repeat from the
                # right child.
                if current_node.right is None:
                    current_node.right = node
                    current_node = None
                else:
                    current_node = current_node.right
    
    def insert_all(self, keys):
        for key in keys:
            self.insert(Node(key))
    
    @staticmethod
    def parse(tree_str):
        # A node is enclosed in parentheses with a either just a key: (key), or 
        # a key, left child, and right child triplet: (key, left, right). The 
        # left and right children, if present, can be either a nested node or 
        # "None".
        #
        # Remove whitespace on ends first
        tree_str = tree_str.strip()
        #
        # The string must be non-empty, start with "(", and end with ")"
        if tree_str == "" or tree_str[0] != "(" or tree_str[-1] != ")":
            return None
        # Parse between parentheses
        tree_str = tree_str[1:-1]
        # Find non-nested commas
        comma_indices = []
        paren_counter = 0
        for i in range(len(tree_str)):
            character = tree_str[i]
            if character == '(':
                paren_counter += 1
            elif character == ')':
                paren_counter -= 1
            elif character == ',' and paren_counter == 0:
                comma_indices.append(i)
        # If no commas, tree_str is expected to be just the node's key
        if len(comma_indices) == 0:
            return Node(int(tree_str))
        # If number of commas is not 2, then the string's format is invalid
        if len(comma_indices) != 2:
            return None
        # "Split" on comma
        i1 = comma_indices[0]
        i2 = comma_indices[1]
        pieces = [tree_str[0:i1], tree_str[i1+1:i2], tree_str[i2+1:]]
        # Make the node with just the key
        node_to_return = Node(int(pieces[0]))
        # Recursively parse children
        node_to_return.left = Node.parse(pieces[1])
        node_to_return.right = Node.parse(pieces[2])
        return node_to_return