def solution(k, tangerine):
    answer = 0
    box = {}
    for t in tangerine:
        if t not in box:
            box[t] = 1
        else:
            box[t] += 1
    for i, j in sorted(box.items(), key=lambda x: x[1], reverse=True):
        k -= j
        answer += 1
        if k <= 0:
            return answer
    return answer