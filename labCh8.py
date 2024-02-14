#8.7
""" def fibonacci(n):
    if n < 0:
        return -1
    elif n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}') """


#8.8
""" def print_all_permutations(permList, nameList):
    if len(nameList) == 0:
        print(', '.join(permList))
    else:
        for i, el in enumerate(nameList):
            permList.append(el)
            nameList.pop(i)

            print_all_permutations(permList, nameList)

            nameList.insert(i, el)
            permList.pop()


if __name__ == "__main__": 
    nameList = input().split(' ')
    permList = []
    print_all_permutations(permList, nameList) """


#8.9
""" def print_num_pattern(num, subtract_by):
    '''Given a positive integer as input (Ex: 12), subtract another positive integer (Ex: 3) continually until a negative value is reached, 
    then continually add the second integer until the first integer is again reached. For this lab, do not end output with a newline and do not use loops.'''

    if num < 0:
        #printing first negative number and returning
        print(num, end=" ")
        return
    #prints first num then each recursive call prints num - subtract_by 
    print(num, end=" ")
    print_num_pattern(num - subtract_by, subtract_by)
    #after recursion returns, prints subtracted numbers in reverse
    print(num, end=' ')

if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2) 

if print_num_pattern(12,3)->
12-3 call 1
    9-3 rec call 1
        6-3 rec call 2
            3-3 rec call 3
                0-3 rec call 4
                -3-3 returning
                0-3 returning
            3-3 returning
        6-3 returning
    9-3 returning
12-3 returning
12 9 6 3 0 -3 0 3 6 9 12 
"""


#8.10
""" def digit_count(num, count = 1):
    '''Takes a positive integer as a parameter and returns the number of digits in the integer.'''
    #base case if num == one digit
    if num // 10 <= 0:
        return count
    #divide num by ten and increment count for each new call
    else:
        return digit_count(num // 10, count + 1)

if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit) """


#8.11
""" def draw_triangle(length, count = 0):
    '''Requirements: Write a recursive function called draw_triangle() that outputs lines of '*' to form a right side up isosceles triangle. 
    Function draw_triangle() has one parameter, an integer representing the base length of the triangle. Assume the base length is always odd and less than 20. 
    Output 9 spaces before the first '*' on the first line for correct formatting. No space is output before the first '*' on the last line when the base length is 19.'''
    symbol = '*'
    if count == length//2:
        print(f'         {symbol * (length - count * 2)}')
    else:
        draw_triangle(length, count + 1)
        if length == 19:
            print(f'{" " * (count)}{symbol * (length - count * 2)}')
        else:
            print(f'{" " * (9 - (length // 2) + count)}{symbol * (length - count * 2)}')
        

if __name__ == '__main__':
    base_length = int(input())
    draw_triangle(base_length) """


#8.12
'''Requirements: Write a recursive function called print_list() that outputs the integer value of each node in a linked list. 
Function print_list() has one parameter, the head node of a list. The main program reads the size of the linked list, followed by the values in the list. 
Assume the linked list has at least 1 node. Output the value of the current node, then call the print_list() function repeatedly until the end of the list is reached. 
Refer to the Node class to explore any available instance methods that can be used for implementing the print_list() function.'''

""" class Node:
    def __init__(self, value):
        self.data_val = value
        self.next_node = None

    def insert_after(self, node):
        tmp_node = self.next_node
        self.next_node = node
        node.next_node = tmp_node

    def get_next(self):
        return self.next_node

    def print_data(self):
        print(self.data_val, end=", ")


def print_list(head):
    if head.get_next() == None:
        head.print_data()
    else:
        head.print_data()
        print_list(head.get_next())

        
if __name__ == "__main__":
    size = int(input())
    value = int(input())
    head_node = Node(value) # Make head node as the first node
    last_node = head_node
    
    # Insert the second and the rest of the nodes
    for n in range(1, size):
        value = int(input())
        new_node = Node(value)
        last_node.insert_after(new_node)
        last_node = new_node
    
    print_list(head_node) """


value = 12
carry = value // 10
new_value = value % 10

print(f'carry {carry} value {new_value}')

