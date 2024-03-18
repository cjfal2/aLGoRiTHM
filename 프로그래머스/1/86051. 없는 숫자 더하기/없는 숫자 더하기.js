function solution(numbers) {
    let answer = 45;
    for (num of numbers) {
        answer = answer - num
    }
    return answer;
}