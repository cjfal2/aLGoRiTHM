from itertools import combinations

N, M = map(int, input().split())
arr = [set() for _ in range(N + 1)]
for _ in range(M):
    l, r = map(int, input().split())
    arr[l].add(r)

answer = 0
for a, b in combinations(range(1, N + 1), 2):
    temp = arr[a] & arr[b]
    if len(temp) >= 2:
        answer += len(temp) * (len(temp) - 1) // 2

print(answer)
