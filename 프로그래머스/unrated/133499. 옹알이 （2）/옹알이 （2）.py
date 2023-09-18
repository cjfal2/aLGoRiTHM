def solution(babbling):
    answer = 0
    temp = {
            "aya": "A",
            "ye": "B",
            "woo": "C",
            "ma": "D"
           }
    
    arr = []
    for w in babbling:
        q = w
        for a in ("aya", "ye", "woo", "ma"):
            q = q.replace(a, temp.get(a))

        arr.append(q)
            

    for w in arr:
        n = len(w)
        if n == 1:
            if w[0] in "ABCD":
                answer += 1
        else:
            for i in range(1, n):
                if w[i] == w[i-1] or w[i] not in "ABCD" or w[i-1] not in "ABCD":
                    break
            else:
                answer += 1
                
    return answer