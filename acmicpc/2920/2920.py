nums = list(map(int,input().split()))
ascending = True
descending = True
for i in range(len(nums)-1):
    if nums[i] + 1 == nums[i+1]:
        descending = False
    elif nums[i] == nums[i+1] +1:
        ascending = False
    else : 
        ascending = False
        descending = False
if ascending: print("ascending")
elif descending: print("descending")
else: print("mixed")
