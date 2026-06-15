def quick_sort (nums: list[int],low:int,high:int) -> None:
    if low < high:
        middleIndex = partition(nums,low,high)
        left = quick_sort(nums,low,middleIndex - 1)
        right = quick_sort(nums,middleIndex+1,high)
        pass
    

def partition (nums: list[int],low:int,high:int) ->int:
    pivot = nums[high]
    i = low
    for j in range(low,high):
        if nums[j] < pivot:
             nums[i],nums[j]=nums[j],nums[i]
             i += 1
            

    nums[i] ,nums[high] = nums[high],nums[i]
    return i

array = [12,20,100,35,55,123,55]
quick_sort(array,0,len(array)-1)
print(array)

    