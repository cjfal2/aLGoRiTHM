while 1:
    N=int(input())
    if N==0:
        break
    arr = list(map(int, input().split()))
    mary = 0
    john = 0
    for a in arr:
        if a:
            john += 1
        else:
            mary += 1
    print(f'Mary won {mary} times and John won {john} times')