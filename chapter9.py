from timeit import default_timer as timer


#9.6.1 - Selection sort - O(n^2)
def selection_sort(arr):
    #loops through entire list
    for i in range(len(arr) - 1):
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
        print(arr)
    return arr


#9.7.1 - Insertion sort - O(n^2) worst case, O(n) best case
def insertion_sort(arr):
    #begin outer loop at idx 1, to be able to switch value to idx 0 if lower.
    for i in range(1, len(arr) - 1):
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


#book ch.4 - Bubble sort - O(n^2)
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


#9.8 - Quick sort - O(n*log(n))
def quick_sort(start, end, array):
    #base case
    if start < end:
        #spot to divide array
        pivot = partition(start, end, array)
        #left array
        quick_sort(start, pivot, array)
        #right array
        quick_sort(pivot + 1, end, array)

#Book - Quick select - O(n)
def quick_select(nth_lowest, start, end, array):
    #base case
    if end - start <= 0:
        #if the partitioned array has only one element, nth_lowest has to be that value 
        return array[start]
    else:
        #partition array from middle, sorting lower values to left and higher values to right
        pivot_pos = partition(start, end, array)
         
        if nth_lowest < pivot_pos:
            #call quick_select for left of pivot_pos until index is found (lower than pivot_pos) 
            return quick_select(nth_lowest, start, pivot_pos - 1, array)
        elif nth_lowest > pivot_pos:
            #call quick_select for right of pivot_pos until index is found (higher than pivot_pos)
            return quick_select(nth_lowest, pivot_pos + 1, end, array)
        else:
            #if pivotpos is in same spot as nth_lowest after the partition, index is found.
            return array[pivot_pos]

#partition helper for quicksort/quickselect - O(n) 
def partition(start, end, array):
    pivotPos = start + (end - start) // 2
    pivot = array[pivotPos]

    while True:
        while array[start] < pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start >= end:
            break
        else:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1
    
    return end

#9.9 Merge sort - O(n*log(n))
def merge_sort(arr, left, right):
    mid = 0
    if left < right:
        #midpoint of partition
        mid = (left + right) // 2
        #recursively sort left and right side
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        #merge left and right side in order
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    #size of partition
    part_size = right - left + 1
    #temp array for merged nums
    merged_nums = [0 for _ in range(part_size)]
    #position to insert into merged nums
    merge_pos = 0
    #init left partition start position
    left_pos = left
    #init right partition start position
    right_pos = mid + 1
    #add smallest element to merged nums
    while left_pos <= mid and right_pos <= right:
        if arr[left_pos] < arr[right_pos]:
            merged_nums[merge_pos] = arr[left_pos]
            left_pos += 1
        else:
            merged_nums[merge_pos] = arr[right_pos]
            right_pos += 1
        merge_pos += 1
    #if left pointer not to end of array
    while left_pos <= mid:
        merged_nums[merge_pos] = arr[left_pos]
        left_pos += 1
        merge_pos += 1
    #if right pointer not to end of array
    while right_pos <= right:
        merged_nums[merge_pos] = arr[right_pos]
        right_pos += 1   
        merge_pos += 1
    #copy merged nums back to original array
    merge_pos = 0
    while merge_pos < part_size:
        arr[left + merge_pos] = merged_nums[merge_pos]
        merge_pos += 1

#9.14.1 LAB: Binary Search - O(log(n))
def binary_search(array, target, left, right):
    mid = left + (right - left) // 2
    if target == array[mid]:
        return mid
    elif left == right:
        return -1
    else:
        if array[mid] < target:
            return binary_search(array, target, mid + 1, right)
        else:
            return binary_search(array, target, left, mid - 1)



if __name__ == '__main__':
    nums = [18, 12, 6, 2, 4, 3, 5, 1, 7, 0, 14]
    #print('Unsorted array:', nums)
    start = timer()
    #selection_sort(nums)
    #insertion_sort(nums)
    #bubble_sort(nums)
    quick_sort(0, len(nums) - 1, nums)
    #pos = quick_select(8, 0, len(nums) - 1, nums)
    #merge_sort(nums, 0, len(nums) - 1)
    #pos = binary_search(nums, 12, 0, len(nums) - 1)
    print(nums)
    #print(pos)
    end = timer() 
    time = end - start

    #print('Sorted array:', nums)
    print(f'Seconds taken: {time:.10f}')




