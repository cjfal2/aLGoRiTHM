const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `9
    5 12 7 10 9 1 2 3 11
    13
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
const inputArray = input().trim().split(" ").map(Number);
inputArray.sort((a, b) => a - b);
const target = parseInt(input());

let answer = 0;
let left = 0;
let right = N - 1;

while (left < right) {
  const plus = inputArray[left] + inputArray[right];

  if (plus === target) {
    answer++;
    left++;
    right--;
  } else if (plus < target) {
    left++;
  } else {
    // plus > target
    right--;
  }
}

console.log(answer);
