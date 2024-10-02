def water_time(test):
    results = []
    for bottles in test:
        empty = sum(1 for b in bottles if b == 0)
        if empty >= 2:
            results.append("Water filling time")
        else:
            results.append("Not now")
    
    return results

T = int(input())
test = []
for _ in range(T):
    bottles = list(map(int, input().split()))
    test.append(bottles)

results = water_time(test)

for result in results:
    print(result)
