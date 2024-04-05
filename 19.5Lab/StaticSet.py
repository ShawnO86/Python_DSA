class StaticSet:
    # Initializes the StaticSet by creating a set with the elements of the argument
    def __init__(self, elements):
        self.elements = set()
        for element in elements:
            self.elements.add(element)

    def __str__(self):
        return "{" + ', '.join([str(elt) for elt in self.elements]) + "}"

    def contains(self, element):
        return element in self.elements

    def get_size(self, ):
        return len(self.elements)

    def print(self, output, separator):
        print(self.elements, file=output, sep=separator)

    # Returns a StaticSet containing every element from self.elements and every
    # element from other_set.
    def union(self, other_set):
        # Replace the next line with your code.
        newSet = set(self.elements)
        for ele in other_set.elements:
            newSet.add(ele)

        return StaticSet(newSet)

    # Returns a StaticSet containing each element from self.elements that is also
    # in other_set.
    def intersection(self, other_set):
        # Replace the next line with your code.
        newSet = set()
        for ele in other_set.elements:
            if ele in self.elements:
                newSet.add(ele)

        return StaticSet(newSet)

    # Returns a StaticSet containing each element from self.elements that is not
    # in other_set.
    def difference(self, other_set):
        # Replace the next line with your code.
        newSet = set()
        for ele in self.elements:
            if ele not in other_set.elements:
                newSet.add(ele)

        return StaticSet(newSet)

    # Returns a StaticSet containing each element from self.elements that
    # satisfies the predicate.
    # - If predicate(element) returns True, element satisfies the predicate.
    # - If predicate(element) returns False, element does not satisfy the predicate.
    def filter(self, predicate):
        # Replace the next line with your code.
        newSet = set()
        for ele in self.elements:
            if predicate(ele) == True:
                newSet.add(ele)

        return StaticSet(newSet)

    # Calls map_function(element) for each element in self.elements and adds the returned
    # value to a StaticSet. After map_function has been called for each element
    # in self.elements, the StaticSet is returned.
    def map(self, map_function):
        newSet = set()
        for ele in self.elements:
            newEle = map_function(ele)
            newSet.add(newEle)
        # Replace the next line with your code.
        return StaticSet(newSet)
