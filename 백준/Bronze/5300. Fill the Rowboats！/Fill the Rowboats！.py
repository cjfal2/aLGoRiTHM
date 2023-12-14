n=int(input())
z = 0
for i in range(1, n+1):
    z += 1
    if z == 6:
        print(i, "Go!", end = " ")
        z = 0
    else:
        print(i, end = " ")
if n % 6:
    print("Go!")