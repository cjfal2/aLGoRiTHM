function solution(arr)
{
    var answer = [];

    for (let i = 0; i < arr.length; i++) {
        if (i === 0) {
            answer.push(arr[i])
        } else if (arr[i] !== answer[answer.length-1]) {
            answer.push(arr[i])
        }
    }
    return answer;
}