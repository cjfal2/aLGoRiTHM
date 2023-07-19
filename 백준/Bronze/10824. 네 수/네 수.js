const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `10 20 30 40
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [A, B, C, D] = input().trim().split(" ");
const num1 = parseInt(A + B)
const num2 = parseInt(C + D)
console.log(num1 + num2)
