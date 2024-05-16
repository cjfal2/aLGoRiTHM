n = int(input())
temp = []
if n % 2:
    n = n//2 + 1
    print(n*(n+1))
else:
    n = n//2 + 1
    print(n*n)
