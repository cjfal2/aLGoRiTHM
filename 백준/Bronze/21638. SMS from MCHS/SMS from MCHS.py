def solve():
    # 폭풍 경고 조건
    if t2 < 0 and v2 >= 10:
        return "A storm warning for tomorrow! Be careful and stay home if possible!"
    
    # 한파 경고 조건
    if t2 < t1:
        return "MCHS warns! Low temperature is expected tomorrow."
    
    # 강풍 경고 조건
    if v2 > v1:
        return "MCHS warns! Strong wind is expected tomorrow."
    
    # 메시지 없음
    return "No message"


t1, v1 = map(int, input().split())
t2, v2 = map(int, input().split())
print(solve())