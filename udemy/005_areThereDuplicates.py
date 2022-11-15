def are_there_duplicates(*args):
    a = set(args)
    b = args
    if len(a) != len(b):
        return print(True)
    else: return print(False)

are_there_duplicates(1, 2, 3) # false
are_there_duplicates(1, 2, 2) # true 
are_there_duplicates('a', 'b', 'c', 'a') # true 