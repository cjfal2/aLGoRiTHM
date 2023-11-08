function solution(n, m, section) {
    let answer = 1; // 페인트칠 수
    let where = section[0]; // 현 위치
    
    section.forEach(e => {
        if (where + m < e + 1) {
            where = e
            answer++
        }
    })
    
    return answer;
}