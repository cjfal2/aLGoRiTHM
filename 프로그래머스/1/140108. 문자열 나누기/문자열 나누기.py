def solution(s):
    answer = 0
    idx = 0
    flag = 1
    N = len(s)
    while idx < N:
        what = s[idx]
        num = 1
        other = 0
        if idx == N - 1:
            answer += 1
            break
        
        while idx < N:
            if idx == len(s) - 1:
                flag = 0
                break
                
            idx += 1
            if s[idx] == what:
                num += 1
            else:
                other += 1
                
            if other == num:
                answer += 1
                break
        if flag:
            idx += 1
    return answer