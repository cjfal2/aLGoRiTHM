function solution(a, b) {
    let aa = 0
    let bb = 0
    if (a<=b) {
        aa = a
        bb = b
    } else {
        aa = b
        bb = a
    }
    let answer = 0
    for (let n = aa; n < bb+1; n++) {
        answer += n
    }
    return answer;
}