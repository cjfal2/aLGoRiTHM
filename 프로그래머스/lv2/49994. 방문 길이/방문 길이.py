def solution(dirs):
    answer = set()
    pan = [[0 for _ in range(11)] for _ in range(11)]
    udrl = {
        "U": (-1, 0),
        "D": (1, 0),
        "R": (0, 1),
        "L": (0, -1),
    }
    x, y = 5, 5
    for w in dirs:
        t = udrl.get(w)
        
        a = x + t[0]
        b = y + t[1]
        if a < 0 or a >= 11 or b < 0 or b >= 11:
            continue
            
        L = [(x, y), (a, b)]
        L.sort(key = lambda x: (x[0], x[1]))
        L = tuple(L)

        if L not in answer:
            answer.add(L)
        x, y = a, b
    return len(answer)