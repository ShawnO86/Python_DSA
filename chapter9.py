#9.6.1 - selection sort
""" nums = [19, 42, 69, 420, 88, 99, 13, 1, 3, 2]
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
    nums[index_smallest] = temp """


