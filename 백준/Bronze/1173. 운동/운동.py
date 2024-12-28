def solve():
    N, m, M, T, R = map(int, input().split())
  
    if m + T > M:
        return -1

    current_pulse = m
    time = 0
    exercise_minutes = 0

    while exercise_minutes < N:
        if current_pulse + T <= M:
            current_pulse += T
            exercise_minutes += 1
        else:
            current_pulse = max(m, current_pulse - R)
        time += 1

    return time


if __name__ == "__main__":
    print(solve())
