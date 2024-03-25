function solution(s) {
    const n = s.length;
    if (n === 4 || n === 6) {
        for (const w of s) {
            if (!"0123456789".includes(w)) {
                return false;
            }
        }
        return true;
    }
    else {
        return false;
    }
}