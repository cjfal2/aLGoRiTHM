function solution(arr) {
    let m = 999999999999999
    arr.forEach (element => {
        if (m > element) {
            m = element
        }
    })
    let answer = []
    arr.forEach (ele => {
        if (ele !== m) {
            answer.push(ele)
        }
    })
    if (answer.length === 0) {
        answer.push(-1)
    }
    return answer;
}