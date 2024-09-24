import math

R, C, N = map(int, input().split())
garo = math.ceil(R / N)
sero = math.ceil(C / N)
print(garo * sero)