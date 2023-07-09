const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input().trim())
const memo = Array.from(Array(N+1), () => Array(10).fill(BigInt(0)))
for (let k = 1; k < 10; k++) {
  memo[1][k] = BigInt(1)
}


for (let i = 2; i < N+1; i++) {
  for (let j = 0; j < 10; j++) {
    if (j === 0) {
      memo[i][j] = memo[i-1][1]
    } else if (j === 9) {
      memo[i][j] = memo[i-1][8]
    } else {
      memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1]
    }
  }
}


let answer = BigInt(0)
memo[N].forEach((e) => {
  answer += e
})
console.log(Number(answer%BigInt(1000000000)))