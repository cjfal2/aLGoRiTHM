def solution(s):
    s = ' '+s
    answer = ''
    print(s)
    for w in range(1, len(s)):
        a = s[w]
        if s[w-1] == ' ':
            a = s[w].upper()
        else:
            a = s[w].lower()
        answer += a
    return answer