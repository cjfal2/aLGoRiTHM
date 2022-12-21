function solution(n) {
    const arr = [...String(n)]
    arr.sort(function(a, b)  {
        return b - a
    })
    let nums = ''
    arr.forEach ((num) => {
        nums += num
    })
    var answer = Number(nums)
    return answer
}