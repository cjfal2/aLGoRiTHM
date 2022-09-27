def find(want):
    Q = []
    for i in range(N):
        for j in range(N):
            if L[i][j] == want:
                Q.append([i, j])
    return Q


def cal():
    




N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
pong = find(9)[0]
one = find(1)
two = find(2)
three = find(3)
four = find(4)
five = find(5)
six = find(6)




