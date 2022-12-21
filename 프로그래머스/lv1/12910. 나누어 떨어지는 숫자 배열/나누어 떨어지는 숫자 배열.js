function solution(arr, divisor) {
    let answer = []
    arr.forEach ((element) => {
        let ed = element%divisor
        if (ed === 0) {
            answer.push(element)
        }
    })
    answer.sort(function(a, b)  {
      return a - b
    })
    if (answer.length === 0) {
        answer.push(-1)
    }
    return answer
}