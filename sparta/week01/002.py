def find_max_occurred_alphabet(string):
    #알파뱃 수만큼 빈 배열 생성
    char_array = [0] * 26
    #인풋 알파뱃이 알파뱃일 경우 아스키코드화, 각 배열에 count++
    for char in string:
        if not char.isalpha():
            continue
        char_index = ord(char) - ord('a')
        char_array[char_index] += 1
    #가장 숫자가 큰 인덱스 찾기
    max_index = char_array.index(max(char_array))
    #인덱스 아스키코드 -> 문자화
    return chr(max_index+ord('a'))

result = find_max_occurred_alphabet

print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))