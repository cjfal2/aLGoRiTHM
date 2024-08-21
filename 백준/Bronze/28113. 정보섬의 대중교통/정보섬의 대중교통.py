n,a,b=map(int,input().split())
if a==b:
    print("Anything")
elif n > a:
    print("Bus")
elif a > b:
    print("Subway")
else:
    print("Bus")