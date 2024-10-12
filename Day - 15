def bags(N, K, M):
    capacityperbag = K * M
    
    bneeded = (N + capacityperbag - 1) // capacityperbag
    return bneeded

T = int(input())
for _ in range(T):
    N, K, M = map(int, input().split())
    print(bags(N, K, M))
