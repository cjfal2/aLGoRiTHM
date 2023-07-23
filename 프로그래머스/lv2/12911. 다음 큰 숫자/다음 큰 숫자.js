function solution(n) {
    let bin = 0;
    n.toString(2).split("").forEach((e) => {
        if (e === "1") bin++
    })
    
    
    let answer = n + 1
    while (1) {
        let temp = 0;
        answer.toString(2).split("").forEach((k) => {
            if (k === "1") temp++
        })
        if (temp === bin) return answer;
        answer++
    }
}