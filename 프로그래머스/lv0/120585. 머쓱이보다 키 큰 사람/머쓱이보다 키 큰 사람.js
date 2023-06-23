function solution(array, height) {
    let answer = 0;
    array.forEach(e => {
        if (e > height) answer++
    })
    return answer;
}