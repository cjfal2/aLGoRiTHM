const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5 4
    1 1 1 1 1
    0 1 0 0 1
    1 0 0 0 1
    0 0 0 1 1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

function bfs() {
  const [M, N] = input().trim().split(" ").map(Number);
  const pan = [];
  for (let n = 0; n < N; n++) {
    const arr = input().trim().split(" ").map(Number);
    pan.push(arr);
  }

  const visited = Array.from(Array(N), () => Array(M).fill(0));
  visited[0][0] = 1;
  const q = [[0, 0]];
  const directions = [
    [1, 0],
    [0, 1],
  ];
  while (q.length > 0) {
    const [x, y] = q.shift();
    if (x === N - 1 && y === M - 1) {
      return 1;
    }

    for (const [dx, dy] of directions) {
      const nx = x + dx;
      const ny = y + dy;

      if (
        N > nx &&
        nx >= 0 &&
        M > ny &&
        ny >= 0 &&
        visited[nx][ny] === 0 &&
        pan[nx][ny] === 1
      ) {
        visited[nx][ny] = 1;
        q.push([nx, ny]);
      }
    }
  }
  return 0;
}

console.log(bfs() ? "Yes" : "No");
