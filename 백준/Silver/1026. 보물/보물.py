N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())), reverse=True)
K = 0
for i in range(N):
    K += A[i]*B[i]
print(K)