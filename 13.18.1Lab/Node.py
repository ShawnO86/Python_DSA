class Node:
    # Initializes this node with the specified numerical data value, next
    # pointer, and previous pointer.
    def __init__(self,initial_data,  next_node=None, previous_node=None):
        self.data = initial_data
        self.next = next_node
        self.previous = previous_node

    # Returns this node's data.
    def get_data(self):
        return self.data

    # Sets this node's data.
    def set_data(self, new_data):
        self.data = new_data

    # Gets this node's next pointer.
    def get_next(self):
        return self.next

    # Sets this node's next pointer.
    def set_next(self, new_next):
        self.next = new_next

    # Gets this node's previous pointer.
    def get_previous(self):
        return self.previous

    # Sets this node's previous pointer.
    def set_previous(self, new_previous):
        self.previous = new_previous
