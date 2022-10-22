N = int(input())
if N == 1:
    print('*')
elif N%2: # 홀
    n = N//2 + 1
    m = N//2
    for i in range(N*2):
        if i%2:
            print(' *'*m)
        else:    
            print('* '*n)        
else: # 짝
    n = N//2
    for i in range(N*2):
        if i%2:
            print(' *'*n)
        else:    
            print('* '*n)        