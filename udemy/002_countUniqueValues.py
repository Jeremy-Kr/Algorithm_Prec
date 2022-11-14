def count_unique_values(arr):
    if len(arr) == 0:
        return print(0)
    curr = 0
    for i in range(1,len(arr)):
        if arr[curr] != arr[i]:
            curr += 1
            arr[curr] = arr[i]
    return print(curr+1)

count_unique_values([1,1,1,1,1,2]) # 2
count_unique_values([1,2,3,4,4,4,7,7,12,12,13]) # 7
count_unique_values([]) # 0
count_unique_values([-2,-1,-1,0,1]) # 4