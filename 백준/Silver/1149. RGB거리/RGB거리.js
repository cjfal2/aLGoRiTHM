const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3
    5 5 5
    1 2 2
    1 2 2
`
).trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = parseInt(input());
let inputArray = Array.from(Array(N), () => input().trim().split(" ").map(Number));


for (let h = 1; h < N; h++) {
  inputArray[h][0] += Math.min(inputArray[h-1][1], inputArray[h-1][2])
  inputArray[h][1] += Math.min(inputArray[h-1][0], inputArray[h-1][2])
  inputArray[h][2] += Math.min(inputArray[h-1][1], inputArray[h-1][0])
}

console.log(Math.min(inputArray[N - 1][0], inputArray[N - 1][1], inputArray[N - 1][2]));
