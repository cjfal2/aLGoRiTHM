import sys
input = sys.stdin.readline

N = int(input().strip())
info = []
for _ in range(N):
    num, strike, ball = map(int, input().strip().split())
    info.append((str(num), strike, ball))

def dfs():
    global ans
    if len(L) == 3:
        # print(L)
        flag = False
        k = -1
        for n,ss,bb in info:
            k += 1
            s, b = 0, 0
            for j in range(3):
                if L[j] == int(n[j]):
                    s += 1
                else:
                    if L[j] in list(map(int, n)): 
                        b += 1
            if s == ss and b == bb:
                flag = True
            else:
                flag = False
                break
        if flag:
            ans += 1
        
    for i in range(1, 10):
        if i not in L:
            L.append(i)
            dfs()
            L.pop()

ans = 0
L = []
dfs()
print(ans)
