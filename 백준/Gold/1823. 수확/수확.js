const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5
    1
    3
    1
    5
    2
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const n = parseInt(input()); // 숫자 하나
const inputArray = Array(n)
  .fill(0)
  .map(() => parseInt(input())); // 여러줄 숫자 하나의 입력
const dp = Array.from(Array(n), () => Array(n).fill(0)); // 이차원 배열의 DP

// 벼의 수확 범위와 현재까지의 수확 횟수를 받아 최대 이익을 계산하는 재귀 함수
function getMaxValue(start, end, cnt) {
  if (start === end) {
    return cnt * inputArray[start];
  }

  if (dp[start][end]) {
    return dp[start][end];
  }

  dp[start][end] = Math.max(
    getMaxValue(start + 1, end, cnt + 1) + cnt * inputArray[start],
    getMaxValue(start, end - 1, cnt + 1) + cnt * inputArray[end]
  );

  return dp[start][end];
}

console.log(getMaxValue(0, n - 1, 1));
