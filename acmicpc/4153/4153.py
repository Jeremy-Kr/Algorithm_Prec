while(True):
    nums = list(map(int,input().split()))
    if sum(nums) == 0:
        break
    sorted_nums = sorted(nums)
    if ((sorted_nums[0] ** 2 ) + (sorted_nums[1] ** 2) == sorted_nums[2] ** 2):
        print("right")
    else: print("wrong")