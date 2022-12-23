def solution(s):
    L = list(map(int, s.split()))
    
    answer = str(min(L))+' '+str(max(L))
    return answer