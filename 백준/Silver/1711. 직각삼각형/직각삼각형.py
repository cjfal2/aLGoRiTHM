import sys
input = sys.stdin.readline
from itertools import combinations, permutations
import math

def dfs(start):
    global co
    if len(s) == 3:
        # print(s)
        A = (s[0][0]-s[1][0])**2+(s[0][1]-s[1][1])**2
        B = (s[0][0]-s[2][0])**2+(s[0][1]-s[2][1])**2
        C = (s[2][0]-s[1][0])**2+(s[2][1]-s[1][1])**2
        if A == B+C or B == A+C or C == A+B:
            co += 1
        return

    r = 0
    for i in range(start, N):
        if visited[i] == 0 and r != L[i]:
            visited[i] = 1
            r = L[i]
            s.append(L[i])
            dfs(i)
            s.pop()
            visited[i] = 0

L = []
N = int(input().strip())
for _ in range(N):
    a, b = map(int, input().strip().split())
    L.append((a, b))
co = 0
s = []
visited = [0] * (N+1)
dfs(0)

print(co)