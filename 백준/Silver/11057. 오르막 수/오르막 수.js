const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `100
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input().trim())
const memo = Array(10).fill(BigInt(1))
for (let i = 1; i < N; i++) {
  for (let j = 1; j < 10; j++) {
    memo[j] = memo[j] + memo[j - 1]
  }
}

console.log(Number(memo.reduce((sum, value) => sum + value, BigInt(0)) % BigInt(10007)))