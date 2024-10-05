T = int(input())  # Number of test cases

for _ in range(T):
    P, Q, R, S = map(int, input().split())  # Profits of companies A, B, C, and D
    # Check if any company has a monopoly
    if P > Q + R + S or Q > P + R + S or R > P + Q + S or S > P + Q + R:
        print("YES")
    else:
        print("NO")
