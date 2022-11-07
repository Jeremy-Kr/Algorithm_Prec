input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    int_to_one = 0
    int_to_zero = 0

    if string[0] == 0:
        int_to_one += 1
    else:
        int_to_zero += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]: 
            if string[i + 1] == '0': 
                int_to_one += 1 
            else:
                int_to_zero += 1
                
    return min(int_to_one,int_to_zero)

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)