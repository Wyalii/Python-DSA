def bubble_sort(nums:list[int]) -> list[int]:
    swapping = True
    end = len(nums)
    while swapping == True:
        swapping = False
        for i in range(1,end):
            if nums[i-1] > nums[i]:
                temp = nums[i-1]
                nums[i-1] = nums[i]
                nums[i] = temp
                swapping = True
 
        print(nums)
    return nums

arrayOfNumbers = [12,332,22,10,5]
bubble_sort(arrayOfNumbers)

