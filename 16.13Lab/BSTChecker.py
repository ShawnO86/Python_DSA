# Returns None if root_node is the root of a valid BST.
# If a BST violation occurs, the node causing the violation is returned. Such a 
# node may be one of three things:
# 1. A node in the left subtree of an ancestor with a lesser key
# 2. A node in the right subtree of an ancestor with a greater key
# 3. A node with the left or right attribute referencing an ancestor

def check_bst_validity(root_node):
    def is_valid(node, min_val, max_val, ancestors):
        
        if node is None:
            return None
        else:
            ancestors.add(node)
            
        # Check if current node's child references an ancestor or violates BST property
        if (node.left in ancestors or node.right in ancestors) or \
            (min_val is not None and node.key < min_val) or \
            (max_val is not None and node.key > max_val):
            return node
        
        # Recursively check left and right subtrees
        left_violation = is_valid(node.left, min_val, node.key, ancestors)
        if left_violation:
            return left_violation
        
        right_violation = is_valid(node.right, node.key, max_val, ancestors)
        if right_violation:
            return right_violation
        
        return None
    
    return is_valid(root_node, None, None, set())