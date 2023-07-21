const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3
10 6 5
11
6 8 9 6 8 6 9 6 8 6 9
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input().trim());
const crane = input().trim().split(" ").map(Number)
const M = input().trim();
const boxes = input().trim().split(" ").map(Number)

if (Math.max(...crane) < Math.max(...boxes)) {
  console.log(-1)
  process.exit();
}

crane.sort((a, b) => b - a)
boxes.sort((a, b) => b - a)

let answer = 0
while (boxes.length > 0) {
  crane.forEach((c) => {
    for (let b = 0; b < boxes.length; b++) {
      if (boxes[b] <= c) {
        boxes.splice(b, 1)
        break
      }
    }
  })
  answer++
}
console.log(answer)