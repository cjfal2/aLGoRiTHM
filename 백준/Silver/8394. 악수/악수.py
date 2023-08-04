N = int(input())
L = [1, 1]
for n in range(2, N+1):
    L.append((L[n-1]%10 + L[n-2]%10)%10)
print(L[N])
