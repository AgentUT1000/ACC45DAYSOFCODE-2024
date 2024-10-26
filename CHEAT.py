T = int(input())
results = []
for _ in range(T):
    N = int(input())
    weeks = N // 7
    rema = N % 7
    tuesdays = weeks
    if rema >= 2:
        tuesdays += 1
    results.append(tuesdays)
for result in results:
    print(result)
