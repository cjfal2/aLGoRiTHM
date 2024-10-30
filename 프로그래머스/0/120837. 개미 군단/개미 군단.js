function solution(hp) {
    let answer = 0;
    
    while (true) {
        if (hp >= 5) {
            hp -= 5
            answer++
        }
        else {
            break;
        }
    }
    while (true) {
        if (hp >= 3) {
            hp -= 3
            answer++
        }
        else {
            break;
        }
    }
    
    return answer+hp;
}