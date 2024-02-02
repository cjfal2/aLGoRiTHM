const stdin = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n")
const input = (() => {
    let line = 0
    return () => stdin[line++]
})()

const N = parseInt(input().trim())
for (let i = 0; i < N; i++) {
    let answer = 0
    for (const number of input().trim().split(" ").map(Number)) {
        answer = answer + number
    }
    console.log(answer)
}