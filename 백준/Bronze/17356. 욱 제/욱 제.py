a, b = map(int, input().split())
M = (b - a) / 400
T = 1 / (1+10**M)
print(T)