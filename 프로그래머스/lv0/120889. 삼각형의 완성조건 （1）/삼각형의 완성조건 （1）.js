function solution(sides) {
    let answer = 2;
    sides.sort((a, b) => b - a)
    if (sides[0] < sides[1] + sides[2]) answer = 1
    return answer;
}