from timeit import default_timer as timer


#9.6.1 - selection sort O(n^2)
def selection_sort(arr):
    #loops through entire list
    for i in range(len(arr)):
        #initialize smallest to index i
        index_smallest = i
        #loops through remaining list after index i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index_smallest]:
                #if num is smaller than current smallest, select new smallest
                index_smallest = j
        #save current num at index i to temp
        temp = arr[i]
        #set num at index i to smallest num
        arr[i] = arr[index_smallest]
        #move arr[i] to where smallest num used to be
        arr[index_smallest] = temp
    return arr


#9.7.1 - insertion sort - O(n^2) worst case, O(n) best case
def insertion_sort(arr):
    #begin outer loop at idx 1, will switch value to idx 0 if temp is lower.
    for i in range(1, len(arr)):
        #initialize unsorted position
        pos = i
        #set unsorted value to temp var
        temp = arr[i]
        #check if value to left of [pos] is greater than temp value and not at left end of array (idx 0)
        while pos > 0 and arr[pos - 1] > temp:
            #shift pos value to the left 
            arr[pos] = arr[pos - 1]
            #decrement position
            pos -= 1
        #insert temp value at [pos]
        arr[pos] = temp
    return arr


#book ch.4 - bubble sort O(n^2)
def bubble_sort(arr):
    #keeps track of last unsorted index
    unsorted_idx = len(arr) - 1
    #keeps track of array being fully sorted
    sorted = False
    #loop until array is sorted
    while not sorted:
        #if passthrough without any swaps, array is sorted
        sorted = True
        #starts at idx 0 to idx that has not been sorted
        for i in range(unsorted_idx):
            #compare pairs of adjacent values and swap them if not in ascending order
            if arr[i] > arr[i + 1]:
                #if a swap happens, the array is not fully sorted
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        #remove sorted value from unsorted index
        unsorted_idx = unsorted_idx - 1
    return arr


#9.8 - quck sort O(n*log(n))
def quickSort(arr, left, right):
    #base case: subarray has 1 or 0 elements
    if right - left <= 0:
        return
    #obtain pivot index and partition array by last element in left part 
    pos = partition(arr, left, right)
    #partition and sort left of pivot
    quickSort(arr, left, pos - 1)
    #partition and sort right of pivot
    quickSort(arr, pos + 1, right)


def partition(arr, left, right):
    #right most index of array for pivot value
    pivot_index = right
    pivot = arr[pivot_index]
    #start right pointer one before pivot index
    right -= 1

    while True:
        #increment left pointer until the value is equal or greater than pivot value
        while arr[left] < pivot:
            left += 1
        #decrement right pointer until the value is equal or less than pivot value
        while arr[right] > pivot:
            right -= 1
        #check if left pointer has passed right pointer 
        if left >= right:
            '''When left becomes greater than or equal to right in the partition:
            all elements to the left of the pivot are less than or equal to the pivot.
            all elements to the right of the pivot are greater than or equal to the pivot.'''
            break
        else:
            #swap left and right pointer values -- left is greater and right is less than pivot value due to previous while loops
            arr[left], arr[right] = arr[right], arr[left]

    #left is greater than or equal to pivot value, so they get swapped, putting pivot value in the correct place at the end of left partition.
    print('left:', arr[left], 'pivot:', arr[pivot_index])
    print('b:', arr)
    arr[pivot_index], arr[left] = arr[left], arr[pivot_index]
    print('a:', arr)

    return left


if __name__ == '__main__':
    nums = [0, 5, 2, 1, 6, 3]
    print('Unsorted array:', nums)
    start = timer()
    #selection_sort(nums)
    #insertion_sort(nums)
    #bubble_sort(nums)
    quickSort(nums, 0, len(nums) - 1)
    end = timer()
    time = end - start

    print('Sorted array:', nums)
    print(f'Time taken: {time:.8f}ms')




