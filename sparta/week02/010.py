# BOJ 1158

def josephus_problem(n,k):
    result = []
    josephus_list = list(range(1, n+1))
    pop = k - 1
    while josephus_list:
        result.append(josephus_list.pop(pop))
        if len(josephus_list) != 0:
            pop = (pop + (k-1)) % len(josephus_list)
    print("<", ", ".join(map(str, result)), ">", sep='')

# n, k = map(int, input().split())
# josephus_problem(n, k)