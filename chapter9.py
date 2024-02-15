#9.6.1 - selection sort
nums = [19, 42, 69, 420, 88, 99, 13, 1, 3, 2]
def selection_sort(nums):
    #loops through entire list
    for i in range(len(nums)):
        #initialize smallest to index i
        index_smallest = i
        #loops through remaining list after index i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[index_smallest]:
                #if num is smaller than current smallest, set new smallest
                index_smallest = j
        #save current num at index i to temp
        temp = nums[i]
        #set num at index i to smallest num
        nums[i] = nums[index_smallest]
        #move nums[i] to where smallest num used to be
        nums[index_smallest] = temp
        
    return nums


#9.7.1 - insertion sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        # Insert numbers[i] into sorted part 
        # stop once numbers[i] is in correct position
        while j > 0 and nums[j] < nums[j - 1]:
            # Swap numbers[j] and numbers[j - 1]
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
            j = j - 1

    return nums


#book ch.4 - bubble sort
def bubble_sort(nums):
    #keeps track of last unsorted index
    unsorted_idx = len(nums) - 1
    #keeps track of array being fully sorted
    sorted = False
    #loop until array is sorted
    while not sorted:
        #if passthrough without any swaps, array is sorted
        sorted = True
        #starts at idx 0 to idx that has not been sorted
        for i in range(unsorted_idx):
            #compare pairs of adjacent values and swap them if not in ascending order
            if nums[i] > nums[i + 1]:
                #if a swap happens, the array is not fully sorted
                sorted = False
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        #remove sorted value from unsorted index
        unsorted_idx = unsorted_idx - 1





