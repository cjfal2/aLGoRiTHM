function solution(n) {
    let answer = 0
    for (let i = 1; i <= 1000000; i++) {
        if (n%i === 1) {
            answer = i
            break
        }
    }
    return answer
}