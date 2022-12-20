function solution(x) {
    // 숫자를 문자로
    const str = String(x)
    // 문자를 배열로
    const arr = [...str]
    // 배열을 돌며 더하기
    let co = 0
    arr.forEach(element => {
        co += Number(element)
    })
    // co로 나누어 떨어지는지 보기
    if (x%co) {
        var answer = false  
    } else {
        var answer = true
    }
    return answer;
}