x = int(input())
y = int(input())

def quadrant(x, y):
    (print(1) if x > 0 else print(3)) if x * y > 0 else (print(4) if x > 0 else print(2))

quadrant(x,y)