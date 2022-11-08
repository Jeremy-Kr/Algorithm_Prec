numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []


def get_count_of_ways_to_target_by_doing_plus_or_minus(array,temp_sum,temp_idx):
    if temp_idx == len(array):
        result.append(temp_sum)
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array,temp_sum + array[temp_idx], temp_idx +1)
    get_count_of_ways_to_target_by_doing_plus_or_minus(array,temp_sum - array[temp_idx], temp_idx +1)

get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, 0, 0)

print(result.count(target_number))