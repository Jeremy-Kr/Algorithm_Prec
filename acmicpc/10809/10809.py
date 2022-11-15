my_string = input()
char_list = [-1] * 26
for i in range(len(my_string)):
    index = ord(my_string[i]) - 97
    if char_list[index] == -1:
        char_list[index] = i
answer = ""
for idx in char_list:
    answer += f'{idx} '
print(answer[0:len(answer)-1])
