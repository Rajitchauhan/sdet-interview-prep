def second_largest(nums):
    largest = float("-inf")
    second_largest = float("-inf")

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    if second_largest == float("-inf"):
        return None

    return second_largest


nums = [12, 35, 1, 10, 34, 1]
print(second_largest(nums))  # 34


# [8, 3, 8, 5, 2]    # [8, 5]
# [-4, -9, -2, -4]   # [-2, -4]
# [7, 7, 7]          # [7] — sirf ek distinct value

def top_two_distinct(nums):
    pass