def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        co = 0
        for n in range(1, num+1):
            if not num%n:
                co += 1
        if co%2:
            answer -= num
        else:
            answer += num
    return answer