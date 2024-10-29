tc = int(input())
for t in range(tc):
    temp = list(map(int, input().split()))
    print(*temp)
    arr = set(temp)
    a = True if 18 in arr else False
    b = True if 17 in arr else False
    if a and b:
        print('both')
    elif a:
        print('mack')
    elif b:
        print('zack')
    else:
        print('none')
    if t != t-1:
        print()
    else:
        continue