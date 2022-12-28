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

while 1:
    what = list(map(int, input().strip().split()))
    a = what.pop(0)
    if a == 0:
        quit()
    
    s = []
    memo = []
    dfs(0)
    print()