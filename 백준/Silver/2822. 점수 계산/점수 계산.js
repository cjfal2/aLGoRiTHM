const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `20
30
50
48
33
66
0
64
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

// const N = parseInt(input());
// const moneys = input().trim().split(" ").map(Number);
// const ceil = parseInt(input());

const arr = {};
for (let i = 1; i <= 8; i++) {
  const n = parseInt(input());
  arr[i] = n;
}

const values = Object.values(arr).sort((a, b) => b - a);
const topFiveValues = values.slice(0, 5);
const score = topFiveValues.reduce((sum, val) => sum + val, 0);
const keyFiveValues = Object.keys(arr).filter(key => topFiveValues.includes(arr[key]))
keyFiveValues.sort((a, b) => a - b)

console.log(score)
console.log(...keyFiveValues)