from UndoCommand import UndoCommand

class SwapCommand(UndoCommand):
    def __init__(self, source, index1, index2):
        # Type your code here.
        super().__init__()
        self.source_list = source
        self.id_1 = index1
        self.id_2 = index2

    def execute(self):
        # Type your code here.
        self.source_list[self.id_1], self.source_list[self.id_2] = self.source_list[self.id_2], self.source_list[self.id_1]
