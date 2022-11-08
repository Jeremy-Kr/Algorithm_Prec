H, M = map(int, input().split())
def alarm (H,M):
    (print(f'{H+23} {M + 15}') if H == 0 else print(f'{H-1} {M + 15}')) if M - 45 < 0 else print(f'{H} {M-45}')

alarm(H,M)
