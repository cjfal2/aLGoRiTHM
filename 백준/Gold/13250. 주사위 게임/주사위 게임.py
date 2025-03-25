import sys
input = sys.stdin.readline

N = int(input().strip())
E = [0.0] * (N + 7)  # N+6까지 필요하므로 여유롭게 N+7

for i in range(1, N + 1):
    cnt = min(6, i)
    E[i] = 1.0  # 지금 한 번 던짐
    for j in range(1, cnt + 1):
        E[i] += (E[i - j] / 6.0)

print(E[N])
