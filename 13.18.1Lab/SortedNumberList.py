from Node import Node

class SortedNumberList:
    def __init__(self):
        self.head = None
        self.tail = None    

    def insert(self, number):
        '''Inserts the number into the list in the correct position such that the
        list remains sorted in ascending order.'''
        node = Node(number)
        if self.head is None:
            #if list empty, sets head and tail as number
            self.head = node
            self.tail = node
        elif self.head.get_data() >= number:
            #sets head as number
            node.set_next(self.head)
            self.head.set_previous(node)
            self.head = node
        elif self.tail.get_data() <= number:
            #sets tail as number
            self.tail.set_next(node)
            node.set_previous(self.tail)
            self.tail = node
        else:
            #search for spot for number and place in acsending order
            currNode = self.head.get_next()
            while currNode is not None:
                if currNode.get_data() >= number:
                    prevNode = currNode.get_previous()
                    node.set_next(currNode)
                    node.set_previous(prevNode)
                    prevNode.set_next(node)
                    currNode.set_previous(node)
                    break

                currNode = currNode.get_next()



    def remove(self, number):
        '''Removes the node with the specified number value from the list.
        Returns True if node is found and removed, False otherwise.'''
        if self.head is None:
            return False
        elif number < self.head.get_data() or number > self.tail.get_data():
            return False
        
        currNode = self.head 
        while currNode is not None:
            if currNode.get_data() == number:
                prevNode = currNode.get_previous() 
                nextNode = currNode.get_next()

                if nextNode is not None:
                    nextNode.set_previous(prevNode)
                if prevNode is not None:
                    prevNode.set_next(nextNode)
                if currNode is self.head:
                    self.head = nextNode
                if currNode is self.tail:
                    self.tail = prevNode
            
                return True
            
            currNode = currNode.get_next()

        return False