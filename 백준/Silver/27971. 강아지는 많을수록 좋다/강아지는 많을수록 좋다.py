N, M, A, B = map(int, input().split())
forbiden = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    for c in range(a, b+1):
        forbiden[c] += 1

dogs = [(0, 0)]
visited = set()
while dogs:
    # print(dogs)
    x, cnt = dogs.pop(0)
    if x == N:
        print(cnt)
        quit()
    for w in (x + A), (x + B):
        if w not in visited and N >= w and not forbiden[w]:
            visited.add(w)
            dogs.append((w, cnt+1))
print(-1)