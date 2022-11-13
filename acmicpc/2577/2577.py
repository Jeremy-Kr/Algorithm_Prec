A = int(input())
B = int(input())
C = int(input())

times = list(map(int, str(A*B*C)))

for i in range(10):
    print(times.count(i))



# times_len = len(times)

# for i in range(10):
#     print(times_len - len(times.replace(str(i),"")))


# sorted_times = sorted(times)

# for i in range(10):
#     print(times.count(str(i)))