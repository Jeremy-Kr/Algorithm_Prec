def valid_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    temp_str1 = {}
    temp_str2 = {}
    for str in str1:
        if str not in temp_str1:
            temp_str1[str] = 1
        else:
            temp_str1[str] += 1
    for str in str2:
        if str not in temp_str2:
            temp_str2[str] = 1
        else:
            temp_str2[str] += 1
    
    if temp_str1 == temp_str2:
        return True
    else: return False

print(valid_anagram('', ''))
print(valid_anagram('aaz', 'zza') )
print(valid_anagram('anagram', 'nagaram'))
print(valid_anagram("rat","car"))
print(valid_anagram('awesome', 'awesom'))
print(valid_anagram('amanaplanacanalpanama', 'acanalmanplanpamana'))
print(valid_anagram('qwerty', 'qeywrt'))
print(valid_anagram('texttwisttime', 'timetwisttext'))