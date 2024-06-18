n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())
ans = []
for i in arr:
    if i % t > 0:
        ans.append(i//t+1)
    else:
        ans.append(i//t)
        
print(sum(ans))
print(n//p, n%p)