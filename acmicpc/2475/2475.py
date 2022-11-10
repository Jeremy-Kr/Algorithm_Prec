nums = list(map(int,input().split()))
squared = list(map(lambda x: x*x , nums))
print(sum(squared)%10)