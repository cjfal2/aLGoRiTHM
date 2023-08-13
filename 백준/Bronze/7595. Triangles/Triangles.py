while 1:
    N = int(input())
    if N == 0:
        break
    for i in range(1, N+1):
        print("*"*i, sep="")