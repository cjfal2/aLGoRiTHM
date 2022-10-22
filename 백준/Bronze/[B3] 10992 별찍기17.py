N = int(input())
if N == 1:
    print('*')
else:
    print(' '*(N-1),'*',sep="")
    for i in range(2, N):
        print(' '*(N-i),'*',' '*(2*i-3),'*', sep='')
    print('*'*(2*N-1))