# t = int(input())
# for _ in range(t):
#     scores = input()
#     # 1 3 6 9 15 피보나치
#     # O인지  아닌지  판별 

#     # X를 만나면 앞의 O를 세어본다 



#     # score = 0
#     # temp = 1
#     # for idx in range(len(scores)):
#     #     if scores[idx] == "O":
#     #         score += temp
#     #         temp += 1
#     #     else:
#     #         temp = 1
#     print(scores)


import sys
N = int(sys.stdin.readline())
for i in range(N):
    quiz_result = sys.stdin.readline()
    accum = 1
    score = 0
    for q in quiz_result:
        if q is 'O':
            score += accum
            accum += 1
        else:
            accum = 1
    print(score)