const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `2147483647 2147483647 100001
  `
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [a, b, c] = input().trim().split(" ").map(BigInt);

function solve(a, b, c) {
  if (b === BigInt(1)) {
    return a % c;
  } else if (b % BigInt(2) === BigInt(0)) {
    return (solve(a, b / BigInt(2), c) ** BigInt(2)) % c;
  } else {
    return ((solve(a, b / BigInt(2), c) ** BigInt(2) * a)) % c;
  }
}

console.log(solve(a, b, c).toString());
