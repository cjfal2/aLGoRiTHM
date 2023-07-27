from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    visited = set(begin)
    q = deque([(begin, 0)])
    while q:
        x, c = q.popleft()
        if x == target:
            return c
        
        for w in words:
            flag = 0
            for y in range(len(target)):
                if x[y] == w[y]:
                    flag += 1
             
            if flag == len(target)-1 and w not in visited and w in words:
                q.append((w, c+1))
                visited.add(w)

    return 0