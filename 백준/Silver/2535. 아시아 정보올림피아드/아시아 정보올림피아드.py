N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[2], reverse=1)

memo = dict()
total = 0
for a, b, c in arr:
    if total == 3:
        break

    if a not in memo:
        memo[a] = 1
        print(a, b)
        total += 1

    else:
        if memo[a] >= 2:
            continue
        else:
            memo[a] += 1
            print(a, b)
            total += 1