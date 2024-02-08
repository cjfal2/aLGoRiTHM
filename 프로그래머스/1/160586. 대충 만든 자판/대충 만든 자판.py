def solution(keymap, targets):
    answer = []
    info = {}
    for k in keymap:
        for j in range(len(k)):
            if k[j] not in info:
                info[k[j]] = j+1
            else:
                info[k[j]] = min(info[k[j]], j+1)
    for t in list(targets):
        temp = 0
        for i in t:
            a = info.get(i)
            if a:
                temp += a
            else:
                temp = -1
                break
        answer.append(temp)
    return answer