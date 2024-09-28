N, A, B, X, Y = map(int, input().split())
k = (N//A+1) * B if N % A else N//A * B
m = (N//X+1) * Y if N % X else N//X * Y
print(min(k, m))