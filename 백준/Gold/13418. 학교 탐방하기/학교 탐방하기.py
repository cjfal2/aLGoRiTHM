import sys
input = sys.stdin.readline

n, m = map(int, input().split())
e = []
for _ in range(m + 1):
    a, b, c = map(int, input().split())
    e.append((c, a, b))
# C: 0(오르막), 1(내리막) — 오르막을 최대/최소로 고르는 MST 두 번 수행
e.sort(key=lambda x: x[0])

# DSU
p = list(range(n + 1))
def find(x):
    # 경로 압축
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x

def union(a, b):
    a = find(a); b = find(b)
    if a == b:
        return False
    p[b] = a
    return True

# 1) 최대 오르막 k_max (오르막 C=0을 우선 선택)
cnt = 0
used = 0
p = list(range(n + 1))
for c, a, b in e:
    if union(a, b):
        if c == 0:
            cnt += 1
        used += 1
        if used == n:
            break
k_max = cnt

# 2) 최소 오르막 k_min (내리막 C=1을 우선 선택)
cnt = 0
used = 0
p = list(range(n + 1))
for c, a, b in reversed(e):
    if union(a, b):
        if c == 0:
            cnt += 1
        used += 1
        if used == n:
            break
k_min = cnt

# 피로도 차이 출력
print(k_max * k_max - k_min * k_min)
