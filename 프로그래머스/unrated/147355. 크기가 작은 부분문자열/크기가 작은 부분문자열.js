function solution(t, p) {
    let answer = 0
    const pLen = p.length
    const tLen = t.length
    
    function cal(str, i, how) {
        return parseInt(str.substring(i, i + how))
    }
    
    for (let idx = 0; idx <= tLen - pLen; idx++) {
        const a = cal(t, idx, pLen)
        if (a <= p) answer++
    }
    
    
    return answer;
}