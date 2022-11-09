h,m = map(int, input().split())
t = int(input())

def oven_timer(h,m,t):
    if t > 59:
        print(f'{h+1} {m+t-60}')
    if m+t < 60:
        print(f'{h} {m+t}')
    else:
        if h+1 > 23:
            print(f'{h-24} {m+t-60}')
        else:
            print(f'{h+1} {m+t-60}')

oven_timer(h,m,t)