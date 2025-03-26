const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `10 6 5
2
10
1
5
9`
).trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, K, B] = input().split(" ").map(Number);
const broken = Array(N + 1).fill(0);

// 고장난 신호등 표시
for (let i = 0; i < B; i++) {
  const idx = parseInt(input());
  broken[idx] = 1;
}

// 초기 구간의 고장 수
let current = 0;
for (let i = 1; i <= K; i++) {
  current += broken[i];
}

let minRepair = current;

// 슬라이딩 윈도우
for (let i = K + 1; i <= N; i++) {
  current += broken[i] - broken[i - K];
  minRepair = Math.min(minRepair, current);
}

console.log(minRepair);
