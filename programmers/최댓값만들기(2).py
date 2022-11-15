# 더 쉬운 방법도 있지만, O(N)을 만들어 보고 싶어서 작성해 보았습니다.

def solution(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    else:
        max1 = max(numbers)
        numbers.remove(max1)
        max2 = max(numbers)
        max_times = max1*max2

        min1 = min(numbers)
        numbers.remove(min1)
        min2 = min(numbers)
        min_times = min1*min2
        
        answer = max(max_times,min_times)
    return answer