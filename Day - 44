def calculate(test_cases):
    durations = []
    for episodes, even_duration, odd_duration in test_cases:
        odd_count = (episodes + 1) // 2
        even_count = episodes // 2
        total_time = (odd_count * odd_duration) + (even_count * even_duration)
        durations.append(total_time)
    return durations

num_test_cases = int(input())
test_cases = []

for _ in range(num_test_cases):
    episodes, even_duration, odd_duration = map(int, input().split())
    test_cases.append((episodes, even_duration, odd_duration))

total_durations = calculate(test_cases)

print()
for duration in total_durations:
    print(duration)
