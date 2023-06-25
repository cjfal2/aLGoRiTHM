const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3 4 5
    3 2
    2 2
    3 1
    2 3
    1 1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const direction = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

const [N, M, K] = input().trim().split(" ").map(Number);

let pan = Array.from(Array(N), () => Array(M).fill("."));

for (let i = 0; i < K; i++) {
  const [A, B] = input().trim().split(" ").map(Number);
  pan[A - 1][B - 1] = "#";
}

let answer = 0;

for (let n = 0; n < N; n++) {
  for (let m = 0; m < M; m++) {
    if (pan[n][m] === "#") {
      let count = 1;
      pan[n][m] = ".";
      let queue = [[n, m]];
      while (queue.length > 0) {
        let deca = queue.shift();
        let x = deca[0];
        let y = deca[1];
        for (let z = 0; z < 4; z++) {
          let nx = x + direction[z][0];
          let ny = y + direction[z][1];
          if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;

          if (pan[nx][ny] === "#") {
            pan[nx][ny] = "."
            queue.push([nx, ny]);
            count++;
          }
        }
      }
      answer = Math.max(answer, count);
    }
  }
}
console.log(answer);
