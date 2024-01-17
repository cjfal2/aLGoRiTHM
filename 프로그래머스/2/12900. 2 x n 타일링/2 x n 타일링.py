def solution(n):
    if n == 1:
        return 1
    
    if n == 2:
        return 2
    
    pan = [0, 1, 2] + [0 for _ in range(n)]
    for i in range(3, n+1):
        pan[i] = (pan[i-2] + pan[i-1]) % 1000000007
    return(pan[n])