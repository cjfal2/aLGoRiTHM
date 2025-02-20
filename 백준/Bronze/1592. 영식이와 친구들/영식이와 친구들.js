const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5 3 2`
)
  .trim()
  .split(" ");

const N = parseInt(stdin[0]);
const M = parseInt(stdin[1]);
const L = parseInt(stdin[2]);

function throwingGame(N, M, L) {
  const counts = new Array(N).fill(0);
  let current = 0;
  let throws = 0;

  counts[current] = 1; // 첫 번째 사람이 공을 받음

  while (counts[current] < M) {
    if (counts[current] % 2 === 1) {
      // 홀수번 받았다면 시계 방향으로 L번째 사람에게 던짐
      current = (current + L) % N;
    } else {
      // 짝수번 받았다면 반시계 방향으로 L번째 사람에게 던짐
      current = (current - L + N) % N;
    }
    counts[current]++;
    throws++;
  }
  return throws;
}

console.log(throwingGame(N, M, L));
