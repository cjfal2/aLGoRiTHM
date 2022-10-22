N = int(input())
if N == 1:
    print('*')
else:
    for i in range(N):
        if i%2:
            print(' *'*N)
        else:    
            print('* '*N)