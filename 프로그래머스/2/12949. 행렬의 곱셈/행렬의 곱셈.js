function solution(arr1, arr2) {
    const n = arr1.length;
    const m = arr2[0].length;
    const k = arr1[0].length;
    
    const answer = Array.from(Array(n), () => Array(m).fill(0));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            for (let t = 0; t < k; t++) {
                answer[i][j] = answer[i][j] + arr1[i][t] * arr2[t][j]
            }
        }
    }
    return answer;
}