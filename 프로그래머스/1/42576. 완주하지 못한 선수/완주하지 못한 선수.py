from collections import Counter 

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)

    p.subtract(c)
    for k, v in p.items():
        if v:
            return k