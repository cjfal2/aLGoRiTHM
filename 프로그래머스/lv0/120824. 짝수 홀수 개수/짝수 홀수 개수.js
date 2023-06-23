function solution(num_list) {
    const answer = [];
    let odd = 0;
    let even = 0;
    num_list.forEach(e => {
        if (e%2) {
            odd++
        } else {
            even++
        }
    })
    answer.push(even)
    answer.push(odd)

    return answer;
}