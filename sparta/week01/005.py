def find_not_repeating_first_character(string):
    char_arr = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        char_idx = ord(char) - ord('a')
        char_arr[char_idx] += 1
    
    not_repeating_character_arr = []
    for idx in range(len(char_arr)):
        if char_arr[idx] == 1:
            not_repeating_character_arr.append(chr(idx + ord('a')))
    for char in string:
        if char in not_repeating_character_arr:
            return char 
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))