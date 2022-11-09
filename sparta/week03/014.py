input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    for i in range(len(input) - 1):
        for j in range(len(input)-1-i):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
    return array
        

bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!