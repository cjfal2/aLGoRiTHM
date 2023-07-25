function solution(people, limit) {
    const len = people.length
    people.sort((a, b) => b - a)
    let answer = 0
    let cut = len - 1 
    for (let p = 0; p <= cut; p++) {
        if (people[p] + people[cut] > limit) {
            answer++
        }
        else {
            cut--
            answer++    
        }
    }
    return answer
}
