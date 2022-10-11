# 시간초과

N = int(input())
A = list(map(int,input().split()))
B = [0] * N
C = list(set(A))
i = -1

for a in A :
    i += 1
    co = 0
    for c in C:
        if a > c :
            co += 1
    B[i] = co
print(*B)