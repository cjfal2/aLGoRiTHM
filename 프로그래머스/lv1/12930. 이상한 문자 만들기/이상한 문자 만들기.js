function solution(s) {
    let answer = '';
    
    const words = s.split(" ")
    
    words.forEach(element => {
        for (let idx = 0; idx < element.length; idx++) {
            if (idx%2 === 0) {
                answer += element[idx].toUpperCase();
            } else {
                answer += element[idx].toLowerCase();
            }
        }
        answer += " "
    })
    
    return answer.substring(0, answer.length - 1);
}