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
    if right - left <= 0:
        return
    pos = partition(arr, left, right)
    quickSort(arr, left, pos - 1)
    quickSort(arr, pos + 1, right)


def partition(arr, left, right):
    pivot_index = right
    pivot = arr[pivot_index]
    right -= 1

    while True:
        while arr[left] < pivot:
            left += 1
            
        while arr[right] > pivot:
            right -= 1

        if left >= right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]

    return left


nums = [7, 3, 1, 2, 15, 44, 22, 33, 44, 82, 240, 354, 12, 32, 99, 1]
start = timer()
#selection_sort(nums)
#insertion_sort(nums)
#bubble_sort(nums)
#quick_sort(nums, 0, len(nums) - 1)
quickSort(nums, 0, len(nums) - 1)
end = timer()

print(nums)
print(end - start)




