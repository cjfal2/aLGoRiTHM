def solution(a, b):
    if len(a) < len(b):
        return 0
    a = a[::-1]
    b = b[::-1]
    for i in range(len(b)):
        if a[i] != b[i]:
            return 0    
    return 1