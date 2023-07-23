function solution(n, m) {
    var answer = [];
    
    a = Math.max(n, m)
    b = Math.min(n, m)
    let i = b
    while (1) {
        if (a%i === 0 && b%i === 0) {
            answer.push(i)
            break
        }
        i--
    }
    let j = a
    while (1) {
        if (j%a === 0 && j%b === 0) {
            answer.push(j)
            break
        }
        j++
    }
    return answer;
}