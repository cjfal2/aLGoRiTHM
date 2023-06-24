function solution(my_string, letter) {
    let answer = [];
    for (let i = 0; i < my_string.length; i++) {
        if (my_string[i] !== letter) {
            answer.push(my_string[i])
        }
    }
    const result = answer.join("")
    return result;
}