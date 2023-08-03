const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3 4
    0001
    0011
    0110
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const directions = [
  [1, 0],
  [-1, 0],
  [0, -1],
  [0, 1],
];
const [N, M] = input().trim().split(" ").map(Number);
const pan = Array.from(Array(N), () => input().trim().split(""));

function bfs(q) {
  while (q.length > 0) {
    const [x, y] = q.shift();
    for (let d = 0; d < 4; d++) {
      const nx = x + directions[d][0];
      const ny = y + directions[d][1];
      if (N > nx && nx >= 0 && M > ny && ny >= 0 && pan[nx][ny] === "0") {
        pan[nx][ny] = pan[x][y] + 1;
        q.push([nx, ny]);
      }
    }
  }
}

const queue = [];
for (let n = 0; n < N; n++) {
  for (let m = 0; m < M; m++) {
    if (pan[n][m] === "1") {
      pan[n][m] = 0;
      queue.push([n, m]);
    }
  }
}
bfs(queue);
pan.forEach((e) => {
  console.log(...e);
});
