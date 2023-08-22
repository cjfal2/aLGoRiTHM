def solution(food):
    answer = ''
    for i, a in enumerate(food[1:], 1):
        for _ in range(a//2):
            answer += str(i)
    return answer + "0" + answer[::-1]