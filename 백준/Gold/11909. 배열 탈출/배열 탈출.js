const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `4
5 2 4 3
6 5 1 2
3 4 5 3
7 4 3 1`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const push = (prev, cur) => {
  return prev > cur ? 0 : cur - prev + 1;
};

const solve = (arr, n) => {
  const dp = Array.from({ length: n }, () => Array(n).fill(0));
  dp[0][0] = 0;

  for (let i = 1; i < 2 * n - 1; i++) {
    const start = Math.floor(i / n) * (i % n + 1);
    for (let j = start; j <= i - start; j++) {
      const curX = j;
      const curY = i - j;

      let rightPath = Number.MAX_SAFE_INTEGER;
      let downPath = Number.MAX_SAFE_INTEGER;

      if (curX > 0) {
        downPath = dp[curX - 1][curY] + push(arr[curX - 1][curY], arr[curX][curY]);
      }
      if (curY > 0) {
        rightPath = dp[curX][curY - 1] + push(arr[curX][curY - 1], arr[curX][curY]);
      }

      dp[curX][curY] = Math.min(rightPath, downPath);
    }
  }

  return dp[n - 1][n - 1];
};

const n = parseInt(input().trim());
const mat = Array.from({ length: n }, () => input().trim().split(" ").map(Number));

console.log(solve(mat, n));
