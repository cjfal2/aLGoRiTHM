N = int(input())
a = 1
for i in range(N-4, N+1):
    a *= i
print(a//120)