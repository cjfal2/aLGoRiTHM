n=int(input())
a,b=map(int,input().split())
a //= 2
print(a+b) if a+b <= n else print(n)