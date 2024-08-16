def solve():
    if N >= M:
        return 0
    
    result = 1
    for i in range(2, N + 1):
        result = (result * i) % M
        if result == 0:
            break
            
    return result


N, M = map(int, input().split())
print(solve())
