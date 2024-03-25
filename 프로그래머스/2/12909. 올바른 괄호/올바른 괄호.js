function solution(s){
    const q = new Array();
    for (const w of s) {
        if (w == "(") {
            q.push(w);
        }
        else {
            if (q.length > 0 && q[q.length-1] === "(") {
                q.pop();
            }
            else {
                return false;
            }
        }
    }
    return q.length > 0 ? false : true;
}

/**
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
*/