q=sorted(map(int,input().split()))
a,b,c=q
if a + b <= c:
    print(0)
elif a == b == c:
    print(2)
elif a**2 + b**2 == c**2:
    print(1)
else:
    print(0)