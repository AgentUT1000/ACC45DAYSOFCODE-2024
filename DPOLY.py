def polynomial(test_cases):
    for t in range(test_cases):
        N = int(input()) 
        coefficients = list(map(int, input().split()))   
        for i in range(N-1, -1, -1):
            if coefficients[i] != 0:
                print(i)
                break

T = int(input())

polynomial(T)
