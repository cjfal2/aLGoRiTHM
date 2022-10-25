N = int(input())
L = [list(map(int, input().split())) for _ in range(N**2)]

base = [[0 for _ in range(N)] for _ in range(N)]
base[1][1] = L[0][0]

