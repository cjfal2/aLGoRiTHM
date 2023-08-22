def solution(s, n):
    answer = ''
    for a in s:
        b = ord(a) + n
        if a == " ":
            answer += " "
        elif a in "QWERTYUIOPASDFGHJKLZXCVBNM":
            if b > 90:
                b = b % 90 + 64
            answer += chr(b) 
        else:
            if b > 122:
                b = b % 122 + 96
            answer += chr(b)
    return answer