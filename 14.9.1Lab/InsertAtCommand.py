from Stack import Stack
from UndoCommand import UndoCommand

class InsertAtCommand(UndoCommand):
    def __init__(self, source, index, new_item):
        # Type your code here.
        super().__init__()
        self.source_list = source
        self.idx = index
        self.new_item = new_item

    def execute(self):
        # Type your code here.
        self.source_list.insert(self.idx, self.new_item)
 
