def solve(cows, start, end):
    if end - start <= 1:
        return 0

    mid = (start + end) // 2
    left_distance = solve(cows, start, mid)
    right_distance = solve(cows, mid, end)

    left_part = cows[start:mid]
    right_part = cows[mid:end]

    swap_distance = 0
    if left_part > right_part:
        cows[start:mid], cows[mid:end] = right_part, left_part
        swap_distance = (end - start) // 2

    return left_distance + right_distance + swap_distance * (end - start)


N = int(input().strip())
cows = [int(input().strip()) for _ in range(2 ** N)]

total_distance = solve(cows, 0, len(cows))

print(total_distance)
for cow in cows:
    print(cow)
