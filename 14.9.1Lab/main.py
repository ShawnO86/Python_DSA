import sys
from GroceryList import GroceryList

def main():
    grocery_list = GroceryList()

    quit = False
    while not quit:
        command = input()

        # Process user input
        if command == "print":
            grocery_list.print_list(sys.stdout)
        elif 0 == command.find("add "):
            grocery_list.add_with_undo(command[4:])
        elif 0 == command.find("removeat "):
            grocery_list.remove_at_with_undo(int(command[9:]))
        elif 0 == command.find("swap "):
            index1, index2 = parse_indices(command[5:])
            if index2 < 0:
                print('"swap" command requires two indices, separated by a space. ex_: swap 2 5')
            else:
                grocery_list.swap_with_undo(index1, index2)
        elif command == "undo":
            if 0 == grocery_list.get_undo_stack_size():
                print("Cannot execute undo because undo stack is empty")
            else:
                grocery_list.execute_undo()
        elif command == "quit":
            quit = True
        else:
            print("unknown command:", command)

def parse_indices(str):
    indices =  [int(n) for n in str.split()]
    if len(indices) != 2:
        return -1, -1
    else:
        return indices

if __name__ == '__main__':
    main()
