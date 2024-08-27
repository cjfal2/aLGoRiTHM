a,b,c=map(int,input().split())
x,y,z=map(int,input().split())
n=a*3+b*20+c*120
k=x*3+y*20+z*120
if n == k:
    print("Draw")
elif n > k:
    print("Max")
else:
    print("Mel")