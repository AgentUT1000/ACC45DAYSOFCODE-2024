T = int(input())
results = []
for _ in range(T):
    A, B, X = map(int, input().split())
    if (B - A) % (2 * X) == 0:
        results.append("YES")
    else:
        results.append("NO")
print("\n".join(results))
