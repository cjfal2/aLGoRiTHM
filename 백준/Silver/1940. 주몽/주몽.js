const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `6
    9
    2 7 4 1 5 3
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
const M = parseInt(input());
const inputArray = input().trim().split(" ").map(Number);
inputArray.sort((a, b) => a - b);

let left = 0;
let right = N - 1;
let answer = 0;
while (left < right) {
  let temp = inputArray[left] + inputArray[right]
  if (temp < M) {
    left++
  } else if (temp > M) {
    right--
  } else {
    answer++
    left++
    right--
  }
}

console.log(answer)