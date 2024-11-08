T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    total_sum = sum(A)
    if abs(total_sum) % 2 != 0:
        print(-1)
    else:
        min_flips = abs(total_sum) // 2
        print(min_flips)
