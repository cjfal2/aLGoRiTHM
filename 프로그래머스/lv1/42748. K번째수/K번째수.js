function solution(array, commands) {
    const answer = [];
    function cal(arr, i, j, k) {
        const temp = arr.slice(i, j+1)
        temp.sort((a, b) => a - b)
        return temp[k]
    }
    
    commands.forEach((e) => {
        answer.push(cal(array, e[0]-1, e[1]-1, e[2]-1))
    })
    
    return answer;
}