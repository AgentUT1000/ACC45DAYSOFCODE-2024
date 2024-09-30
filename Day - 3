def TW_hours(T, test):
    results = []
    
    for case in test:
        X, Y = case
        thours = (4 * X) + Y
        results.append(thours)
    
    return results

T = int(input())
test = [tuple(map(int, input().split())) for _ in range(T)]

results = TW_hours(T, test)

for result in results:
    print(result)
