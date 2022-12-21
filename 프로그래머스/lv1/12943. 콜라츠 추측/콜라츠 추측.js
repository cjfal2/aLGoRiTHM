function solution(num) {
    if (num === 1) {
        return 0
    }
    let n = num
    for (let i = 0; i<500; i++) {
        if (n === 1) {
            return i
        }
        if (n%2) {
            n = n * 3 + 1
        } else {
            n = n/2
        }
    }
    
    return -1;
}