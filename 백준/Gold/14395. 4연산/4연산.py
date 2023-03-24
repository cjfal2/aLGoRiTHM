def cal(p, s):
    if p == "*": return s*s
    elif p == "+": return s+s
    elif p == "-": return s-s
    elif s: return s//s
        
num, end = map(int, input().split())
visited = set([num])
q = [(num,'')]
while q:
    x, info = q.pop(0)
    if x == end:
        print(info) if info else print(0)
        quit()
    for dx in '*+-/':
        nx = cal(dx, x)
        if nx not in visited and 0 < nx <= 10e9:
            visited.add(nx)
            q.append((nx, info+dx))
print(-1)