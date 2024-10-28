T = int(input())
results = []
for _ in range(T):
    N, K = map(int, input().split())
    characteristics = list(map(int, input().split()))
    count = 0
    for value in characteristics:
        value = value + K
        if value % 7 == 0:
            count += 1
    results.append(count)
for result in results:
    print(result)
