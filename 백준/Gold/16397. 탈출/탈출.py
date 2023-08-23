N, T, G = map(int, input().split())
big = 100000

visited = [0 for _ in range(big)]
visited[N] = 1
q = [(N, 0)]

while q:
    where, cnt = q.pop(0)
    if cnt > T:
        print("ANG")
        quit()
    if where == G:
        print(cnt)
        quit()

    A = where + 1
    B = where * 2
    if A < big and not visited[A]:
        q.append((A, cnt+1))
        visited[A] = 1

    if B < big:
        B = str(B)
        if int(B):
            B = str(int(B[0])-1) + B[1:]
        B = int(B)
        if not visited[B]:
            q.append((B, cnt+1))
            visited[B] = 1
            
print("ANG")

