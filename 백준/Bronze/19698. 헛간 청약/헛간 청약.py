N, W, H, L = map(int, input().split())
W //= L
H //= L
a = W * H
print(a) if a <= N else print(N)