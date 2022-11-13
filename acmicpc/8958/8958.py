t = int(input())
for _ in range(t):
    scores = input()
    score = 0
    bonus = 0
    for idx in range(len(scores) ):
        if scores[idx] == "O":
            if scores[idx] == scores[idx-1]:
                score += 1 + bonus
                bonus += 1
            else:
                score += 1
                bonus += 1
        else:
            bonus = 0
    print(score)