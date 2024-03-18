function solution(s) {
    const a = s.length;
    const b = Math.floor(s.length/2);
    if (a%2) {
        return s[b];
    }
    else {
        return s.slice(b-1,b+1);
    }
}