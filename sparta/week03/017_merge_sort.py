array = [5, 3, 2, 1, 6, 8, 7, 4]

#분할 및 정복 단계
def merge_sort(array):
    if len(array) <= 1:
        return array
    #분할단계
    mid = (0+len(array)) // 2
    array1 = array[:mid]
    array2 = array[mid:]
    #정복단계
    return merge(merge_sort(array1), merge_sort(array2))

# 결합단계
def merge(array1, array2):
    result = []
    # len(array1) len(array2) 둘 다 존재할 때
    while len(array1) != 0 and len(array2) != 0 :
        if array1[0] < array2[0]:
            result.append(array1.pop(0))
        else:
            result.append(array2.pop(0))

    # 위 while을 실행하고 array1이 남아있을 때
    while len(array1) != 0 :
        result.append(array1.pop(0))

    # 위 while을 실행하고 array2가 남아있을 때
    while len(array2) != 0 :
        result.append(array2.pop(0))
    
    return result


print(merge_sort(array))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge_sort([-7, -1, 9, 40, 5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge_sort([-1, 2, 3, 5, 40, 10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge_sort([-1, -1, 0, 1, 6, 9, 10]))