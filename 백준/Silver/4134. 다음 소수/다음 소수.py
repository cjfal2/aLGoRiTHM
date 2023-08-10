def prime(num):
    if num == 0 or num == 1:
        return False
    
    if num == 2:
        return True
    
    for i in range(2, int(num**(0.5))+1):
        if not num % i:
            return False
    return True


for _ in range(int(input())):
    N = int(input())
    while 1:
        if prime(N):
            print(N)
            break
        else:
            N += 1
