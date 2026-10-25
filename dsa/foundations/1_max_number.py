def max_number(nums):
    n = len(nums)
    max_number = nums[0]
    for i in range(1 ,n):
        if nums[i] > max_number:
            max_number = nums[i]
    return max_number 




nums = [7, 3, 9, 4, 6]