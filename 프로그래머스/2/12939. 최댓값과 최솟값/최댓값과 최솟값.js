function solution(s) {
    let answer = '';
    
    const numbers = s.split(" ").map(Number);
    
    answer = answer + Math.min(...numbers).toString();
    answer = answer + " ";
    answer = answer + Math.max(...numbers).toString();
    
    return answer;
}