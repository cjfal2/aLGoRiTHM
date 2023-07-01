import sys
ip = sys.stdin.readline

N = int(ip())
L = list(map(int, ip().split()))

big = L
small = L
for _ in range(N - 1):
    L = list(map(int, ip().split()))
    big = [L[0] + max(big[0], big[1]), L[1] + max(big), L[2] + max(big[1], big[2])]
    small = [L[0] + min(small[0], small[1]), L[1] + min(small), L[2] + min(small[1], small[2])]

print(max(big), min(small))