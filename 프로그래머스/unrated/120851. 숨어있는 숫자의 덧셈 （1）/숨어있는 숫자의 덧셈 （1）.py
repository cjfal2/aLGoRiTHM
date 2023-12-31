def solution(my_string):
    answer = 0
    for m in my_string:
        if m in "0123456789":
            answer+=int(m)
    return answer