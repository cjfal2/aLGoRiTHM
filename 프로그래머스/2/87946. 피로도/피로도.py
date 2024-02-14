from itertools import permutations

def solution(k, dungeons):
    N = len(dungeons)
    answer = 0
    for permu in permutations(dungeons, N):
        temp = k
        res = 0 
        for x, y in permu:
            if temp < x:
                break
            temp -= y
            res += 1
        answer = max(answer, res)
    return answer