N, M = int(input()), int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
X = int(input())
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
q = [(0, 0)]
color = pan[0][0]
answer = "DEAD"


def find_block(A, B):
    temp = []
    for a in range(A-X, A+X+1):
        for b in range(B-X, B+X+1):
            if N > a >= 0 and M > b >= 0 and abs(A-a)+abs(B-b) <= X:
                temp.append((a, b))
    return temp


while q:
    x, y = q.pop(0)
    if x == N-1 and y == M-1:
        answer = "ALIVE"
        break

    for nx, ny in find_block(x, y):
        if not visited[nx][ny] and pan[nx][ny] == color:
            q.append((nx, ny))
            visited[nx][ny] = 1

print(answer)
