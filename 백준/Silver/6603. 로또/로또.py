import sys
input = sys.stdin.readline

def dfs(start):
    if len(s) == 6 and s not in memo:
        print(*s)
        memo.append(s[:])
        return
    for i in range(start, len(what)):
        if what[i] not in s:
            s.append(what[i])
            dfs(i)
            s.pop()

z = 0
while 1:
    if not z:
        what = list(map(int, input().strip().split()))
        z += 1
    a = what.pop(0)
    if not a:
        quit()
    
    s = []
    memo = []
    dfs(0)
    if z:
        what = list(map(int, input().strip().split()))
        print()
