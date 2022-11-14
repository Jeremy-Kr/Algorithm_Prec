def same_frequency(num1,num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    if len(str_num1) != len(str_num2):
        return False
    count_nums1 = {}
    count_nums2 = {}
    for str1 in str_num1:
        if str1 not in count_nums1:
            count_nums1[str1] = 1
        else:
            count_nums1[str1] += 1
    
    for str2 in str_num2:
        if str2 not in count_nums2:
            count_nums2[str2] = 1
        else:
            count_nums2[str2] += 1

    if count_nums1 == count_nums2:
        return True
    else: return False

print(same_frequency(182,281)) # true
print(same_frequency(34,14)) # false
print(same_frequency(3589578, 5879385)) # true
print(same_frequency(22,222)) # false
