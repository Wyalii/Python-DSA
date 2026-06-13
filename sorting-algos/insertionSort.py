def insertion_sort(nums:list[int]) -> list[int]:
    for i in range(len(nums)): # this guys is main loop that is ahead of inner loop by indexes
        j = i # i set j to be equal to that index here
        while j > 0 and nums[j-1] > nums[j]: # starting from second element we check if left element is more than right (out of order) 
            temp = nums[j] #we save current variable
            nums[j] = nums[j-1] #we set right element value to the value of left element 
            nums[j-1] = temp #same thing here we set left value to right value 
            j -= 1 #decerement j so that i will keep comparing left side elements

    return nums
    

array = [15,13,27,100,200]
print(insertion_sort(array))