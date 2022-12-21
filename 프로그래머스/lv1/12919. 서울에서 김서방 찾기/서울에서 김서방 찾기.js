function solution(seoul) {
    for (let i = 0; i<1000; i++) {
        if (seoul[i] === 'Kim') {
            return "김서방은 "+String(i)+"에 있다"
        }
    }
}