function solution(arr) {
    let small = 9999999999999;
    for (let num of arr) {
        if (num < small) {
            small = num;
        }
    }
    
    let answer = new Array();
    for (let num of arr) {
        if (num !== small) {
            answer.push(num);
        }
    }
    console.log(answer)
    return answer.length > 0 ? answer : [-1];
}