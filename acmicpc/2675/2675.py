times1 = int(input())
for _ in range(times1):
    times2, input_text = input().split(" ")
    answer = ''.join(list(map(lambda s: s * int(times2), input_text)))
    print(answer)