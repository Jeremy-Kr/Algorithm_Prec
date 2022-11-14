def is_correct_parenthesis(string):
    temp = []
    for i in range(len(string)):
        if string[i] == "(":
            temp.append(i)
        else:
            if len(temp) == 0:
                return False
            else:
                temp.pop()
    if len(temp) != 0:
        return False
    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))