nums = list(input().split())
reversed_list = []

for num in nums:
    reversed_list.append(int(num[::-1]))
print(str(max(reversed_list)))