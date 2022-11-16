t = int(input())
#수학적으로 접근하면 더 잘 풀수 있을거 같음. 다시 고민해보기...
for _ in range(t):
    room_input = list(map(int,input().split()))
    H = room_input[0]
    W = room_input[1]
    N = room_input[2]

    floor = list(range(1,H+1))
    room = list(range(1,W+1))
    rooms = []
    for i in range(len(room)):
        for j in range(len(floor)):
            if room[i] > 9:
                rooms.append(f'{floor[j]}{room[i]}')
            else: 
                rooms.append(f'{floor[j]}0{room[i]}')
    print(rooms[N-1])
    