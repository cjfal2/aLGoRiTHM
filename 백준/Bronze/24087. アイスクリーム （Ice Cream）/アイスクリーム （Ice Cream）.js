const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `28
20
5`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const S = parseInt(input().trim());
const A = parseInt(input().trim());
const B = parseInt(input().trim());

let cost = 250;

if (A < S) {
  const need = Math.ceil((S - A) / B);
  cost += 100 * need;
}

console.log(cost);
