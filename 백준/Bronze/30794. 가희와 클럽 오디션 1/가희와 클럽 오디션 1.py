n,m=input().split()
n=int(n)
if m == "miss":
    n*=0
elif m == "bad":
    n*=200
elif m == "cool":
    n*=400
elif m == "great":
    n*=600
elif m == "perfect":
    n*=1000
print(n)