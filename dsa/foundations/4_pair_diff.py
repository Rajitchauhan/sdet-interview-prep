def has_pair_with_difference(times, target):
    # tumhara code
    
    start , end = 0 , len(times)-1

    while (start < end):
        diff =  times[end] - times[start]
        if diff > target:
            end -= 1 
        elif diff < target:
            start += 1
        elif diff == target:
            return [times[start] , times[end]]

times = [2, 5, 8, 12, 15, 18]
target = 10