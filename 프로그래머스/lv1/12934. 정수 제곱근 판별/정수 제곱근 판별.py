import math

def solution(n):
    i = 0
    while 1:
        i += 1
        if i*i == n:
            return (i+1)**2
            break
        if i > math.sqrt(n):
            return -1