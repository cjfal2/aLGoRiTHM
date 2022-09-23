"""
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
"""


def dfs():
    if len(s) == N-1:
        t = s[:]
        combi.append(t)
        return

    for i in nums:
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()


for tc in range(int(input())):
    N = int(input())
    L = [list(map(int, input().split())) for _ in range(N)]
    nums = list(range(1, N))
    combi = []
    s = []
    dfs()
    print(combi)

    co = 999999
    for com in combi:
        battery = 0
        battery += L[0][com[0]]
        for j in range(len(com)-1):
            battery += L[com[j]][com[j+1]]
        battery += L[com[-1]][0]
        co = min(co, battery)

    print(f'#{tc+1} {co}')
