def solution(ingredient):
    answer = 0
    s = []
    for i in ingredient:
        s.append(i)
        if i == 1 and len(s) >= 4:
            if s[len(s)-2] == 3 and s[len(s)-3] == 2 and s[len(s)-4] == 1:
                answer += 1
                for _ in range(4):
                    s.pop()             
    return answer