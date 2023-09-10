temp = [2 for _ in range(16)]
N = int(input())
for i in range(1, N+1):
   temp[i] = temp[i-1] + temp[i-1]-1
print(temp[N]*temp[N]) 