def solution(s):
    q = []
    for w in s:
        if w=='(':
            q.append(w)
        else:
            if q and q[-1] == '(':
                q.pop()
            else:
                return False
    if q:
        return False
    return True