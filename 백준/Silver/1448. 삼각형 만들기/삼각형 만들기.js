const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5
    4
    5
    6
    7
    20
`
).trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
const inputArray = Array.from(Array(N), () => parseInt(input()));

inputArray.sort((a, b) => b - a)

let answer = -1;
for (let i = 0; i < N-2; i++) {
  let A = inputArray[i]
  let B = inputArray[i+1]
  let C = inputArray[i+2]

  if (A < B+C) {
    answer = A+B+C
    break
  }
}
console.log(answer)