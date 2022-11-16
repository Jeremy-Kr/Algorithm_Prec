n,x = map(int,input().split())
nums = list(map(int,input().split()))

answer = []
answer_string = ""
for i in range(n):
    if x > nums[i]:
        answer.append(nums[i])
for ans in answer:
    answer_string += f'{ans} '

print(answer_string[0:-1])