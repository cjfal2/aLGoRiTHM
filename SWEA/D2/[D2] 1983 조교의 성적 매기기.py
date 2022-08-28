SCORE = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(int(input())):
    N, K = map(int, input().split())
    L = []
    for i in range(1, N+1):
        A, B, C = map(int, input().split())
        A *= 0.35
        B *= 0.45
        C *= 0.2
        T = A+B+C
        L.append([T, i])
    L.sort(reverse=True)
    Q = N//10
    z = -1
    for idx in range(0, N, Q):
        z += 1
        for i in range(Q):
            L[idx+i] += [SCORE[z]]
    x = ''
    for a, b, c in L:
        if b == K:
            x = c
            break
    print(f'#{tc+1} {x}')