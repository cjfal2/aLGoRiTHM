N = int(input())
R = sorted([int(input()) for _ in range(N)], reverse=1)
print(max([R[i] * (i+1) for i in range(N)]))