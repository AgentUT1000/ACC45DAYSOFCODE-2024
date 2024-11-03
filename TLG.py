N = int(input())
p1 = 0
p2 = 0
mlead = 0
winner = 0

for _ in range(N):
    Si, Ti = map(int, input().split())
    
    p1 += Si
    p2 += Ti
    
    if p1 > p2:
        current_lead = p1 - p2
        current_winner = 1
    else:
        current_lead = p2 - p1
        current_winner = 2
    
    if current_lead > mlead:
        mlead = current_lead
        winner = current_winner

print(winner, mlead)
