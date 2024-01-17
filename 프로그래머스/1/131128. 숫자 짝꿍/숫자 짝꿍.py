from collections import Counter


def solution(X, Y):
    answer = []
    x = Counter(X)
    y = Counter(Y)
    for k, v in x.items():
        for a, b in y.items():
            if k == a:
                if v >= b:
                    for _ in range(b):
                        answer.append(a)
                else:
                    for _ in range(v):
                        answer.append(k)
        
    if not answer:
        return "-1"
    
    if set(answer) == {"0"}:
        return "0"
    
    answer.sort(reverse=1)
    return "".join(answer)