from Stack import Stack
from InsertAtCommand import InsertAtCommand
from RemoveLastCommand import RemoveLastCommand
from SwapCommand import SwapCommand

class GroceryList:
    def __init__(self):
        self.list_items = []
        self.undo_stack = Stack()

    def add_with_undo(self, new_item_name):
        # Add the list item
        self.list_items.append(new_item_name)

        # Make an undo command that removes the last item and pushes it onto the undo stack
        self.undo_stack.push(RemoveLastCommand(self.list_items))

    def remove_at_with_undo(self, removal_index):
        # Type your code here.
        removed_item = self.list_items.pop(removal_index)

        #Undo command that inserts removed item 
        self.undo_stack.push(InsertAtCommand(self.list_items, removal_index, removed_item))

    def swap_with_undo(self, index1, index2):
        # Type your code here.
        if index1 < 0 or index1 >= len(self.list_items) or index2 < 0 or index2 >= len(self.list_items):
            # Index out of bounds
            return

        # Swap
        self.list_items[index1], self.list_items[index2] = self.list_items[index2], self.list_items[index1]

        # Make an undo command that swaps back, and pushes it onto the undo stack
        cmd = SwapCommand(self.list_items, index1, index2)
        self.undo_stack.push(cmd)

    def execute_undo(self):
        # Type your code here.
        remove = self.undo_stack.pop()
        remove.execute()    

    def get_list_size(self):
       return len(self.list_items)

    def get_undo_stack_size(self):
       return self.undo_stack.size()

    def get_list_copy(self):
       return self.list_items[:]

    def print_list(self, outfil):
        for n, item in enumerate(self.list_items):
            print(f"""{n}. {item}""", file=outfil)
