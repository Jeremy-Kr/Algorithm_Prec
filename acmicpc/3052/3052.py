nums = []
for _ in range(10):
   nums.append(int(input()))
remainders = []
for num in nums:
    remainders.append(num % 42)

print(len(set(remainders)))