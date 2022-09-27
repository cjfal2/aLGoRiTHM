import sys
sys.stdin = open("s1.txt", 'r')

def joongso(idx, co):
    global ans
    if co <= ans:
        return

    if idx >= N:
        ans = co
        return
    for z in range(N):
        if visited[z] == 1:
            continue
        visited[z] = 1
        joongso(idx+1, co*0.01*L[idx][z])
        visited[z] = 0





for tc in range(int(input())):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    s = []
    ans = 0
    visited = [0] * (N+1)
    joongso(0, 100)
    print(f'#{tc+1} {ans:.6f}')

