function solution(n) {
    let answer = 0;
    const array = [];
    for (let i = 1; i < n+1; i++) {
        array.push(i)
    }
    
    let left = 0
    let right = n-1
    while (left <= right) {
        const temp = array[left] * array[right]

        if (temp === n) {
  
            if (left !== right) answer++
    
            answer++
            left++
            right--
        } else if (temp > n) {
            right--
        } else {
            left++
        }
    }
    
    return answer;
}