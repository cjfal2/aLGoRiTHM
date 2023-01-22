import sys
input = sys.stdin.readline

U, N = map(int, input().strip().split())
info = dict()
for _ in range(N):
    name, call = input().strip().split()
    call = int(call)
    if call not in info:
        info[call] = [name]
    else:
        info[call].append(name)
ans = sorted(info.items(),key = lambda x: (len(x[1]), x[0]))[0]
print(ans[1][0], ans[0])