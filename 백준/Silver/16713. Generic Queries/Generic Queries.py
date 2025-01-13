import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
a = list(map(int, input().split()))

prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i - 1] ^ a[i - 1]

result = 0
for _ in range(Q):
    s, e = map(int, input().split())
    result ^= (prefix[e] ^ prefix[s - 1])

print(result)
