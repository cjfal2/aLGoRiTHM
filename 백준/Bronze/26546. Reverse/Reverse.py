for _ in range(int(input())):
    a,b,c=input().split()
    b = int(b)
    c = int(c)
    print(a[:b], a[c:], sep="")