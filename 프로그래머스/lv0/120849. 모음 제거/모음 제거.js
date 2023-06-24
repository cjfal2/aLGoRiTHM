function solution(my_string) {
    var answer = '';
    const moum = ["a", "i", "u", "e" ,"o"]
    my_string.split("").forEach(e => {
        if (!moum.includes(e)) {
            answer = answer + e
        }
    })
    return answer;
}