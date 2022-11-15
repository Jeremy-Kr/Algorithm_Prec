my_string = input()


upper_string = my_string.upper()
string_dict = {}
for char in upper_string:
    if char not in string_dict :
        string_dict[char] = 1
    else:
        string_dict[char] += 1
nums_char = list(string_dict.values())
max_char = max(nums_char)
if nums_char.count(max_char) != 1:
    print("?")
else:
    for key, value in string_dict.items():
        if value == max_char:
            print(key)


