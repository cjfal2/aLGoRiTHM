function solution(x, n) {
    var answer = [];
    let xxx = 0
    for (var i = 0; i < n; i++) {
        xxx += x
        answer.push(xxx)
    }
    return answer;
}