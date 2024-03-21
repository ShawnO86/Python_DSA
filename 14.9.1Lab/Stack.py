# Simple list implementation of Stack

class Stack:
    def __init__(self):
        self.stack_list = []

    def size(self):
        return len(self.stack_list)

    def pop(self):
        return self.stack_list.pop()

    def push(self, item):
        self.stack_list.append(item)

    def top(self):
        return self.stack_list[-1]

    def items(self):
        return self.stack_list