def max_subarray_sum(arr,num):
    if len(arr) < num:
        return None
    temp_sum = 0
    max_sum = 0
    for i in range(0,num):
        max_sum += arr[i]
    temp_sum = max_sum
    for i in range(num, len(arr)):
        temp_sum = temp_sum - arr[i-num] + arr[i]
        max_sum = max(max_sum, temp_sum)
    return max_sum






max_subarray_sum([2, 6, 9, 2, 1, 8, 5, 6, 3], 3)