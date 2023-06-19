const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `
    6
    5 4 3 2 1 0
`
).trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = parseInt(input());
let inputArray = input().split(" ").map(Number);
let temp = new Array(N).fill(0);

for (let i = 0; i < N; i++) {
  let cnt = 0;

  for (let j = 0; j < N; j++) {
    if (cnt === inputArray[i] && temp[j] === 0) {
      temp[j] = i + 1;
      break;
      
    } else if (temp[j] === 0) {
      cnt += 1;
    }
  }
}

console.log(temp.join(" "));
