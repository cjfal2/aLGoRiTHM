N, M = map(int, input().split())
block = set()
for _ in range(M):
    a, b = map(int, input().split())
    block.add((min(a, b), max(a, b)))

answer = 0
for n in range(1, N-1):
    for m in range(n+1, N):
        for k in range(m+1, N+1):
            # print(n, m, k)
            if (n, m) in block:
                continue
            if (n, k) in block:
                continue
            if (m, k) in block:
                continue
            answer += 1
            # print("***")
print(answer)
