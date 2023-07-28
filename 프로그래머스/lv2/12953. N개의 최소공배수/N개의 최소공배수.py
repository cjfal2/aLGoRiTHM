def solution(arr):
    num = max(arr)
    while 1:
        flag = 0
        for a in arr:
            if not num % a:
                flag += 1
        if flag == len(arr):
            break
        num += 1
    return num