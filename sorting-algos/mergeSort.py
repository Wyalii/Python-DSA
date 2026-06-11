def merge_sort(nums: list[int]) -> list[int]:
    
    if len(nums) > 1:
        mid = len(nums)//2
        leftSide = nums[:mid]
        rightSide = nums[mid:]
        merge_sort(leftSide)
        merge_sort(rightSide)

        i=j=k=0
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                nums[k] = leftSide[i]
                i+=1
            else:
                nums[k] = rightSide[j]
                j += 1 

            k+=1    

            while i < len(leftSide):
             nums[k] = leftSide[i]
             i += 1
             k += 1
 
        while j < len(rightSide):
            nums[k] = rightSide[j]
            j += 1
            k += 1
        
    
                   

    pass


array = [20,15,10]
merge_sort(array)
print('sorted array:', array)