import math

def cal_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def bfs(s, e, power):
    q = [(s, e, power)]
    visited = set()
    visited.add((s, e))
    result = 1
    while q:
        x, y, call_power = q.pop(0)
        for new_where, np in cows.items():
            if new_where not in visited and cal_distance(x, y, *new_where) <= call_power:
                visited.add(new_where)
                q.append((*new_where, np))
                result += 1
    return result

N = int(input())
cows = dict()
for _ in range(N):
    x, y, p = map(int, input().split())
    cows[(x, y)] = p

answer = 0
for where, p in cows.items():
    res = bfs(*where, p)
    answer = max(answer, res)
print(answer)
