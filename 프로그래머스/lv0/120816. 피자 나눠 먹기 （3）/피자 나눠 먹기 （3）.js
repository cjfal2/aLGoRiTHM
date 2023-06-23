function solution(slice, n) {
    let answer = 0;
    while (true) {
        answer++
        if (slice*answer >= n) break
    }
    
    return answer;
}