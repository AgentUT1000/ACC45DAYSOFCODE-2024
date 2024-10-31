T = int(input())
for _ in range(T):
    P, Q = map(int, input().split())
    totpo = P + Q
    if (totpo // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")
