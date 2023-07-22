const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3 4
    RRDD
    RRDR
    DULU
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().trim().split(" ").map(Number);
const pan = Array.from(Array(N), () => "");
for (let k = 0; k < N; k++) {
  pan[k] = input().trim();
}
const visited = Array.from(Array(N), () => Array(M).fill(-1));
const directions = {
  U: [-1, 0],
  R: [0, 1],
  D: [1, 0],
  L: [0, -1],
};

function dfs(x, y) {
  if (N <= x || 0 > x || M <= y || 0 > y) return 1; // 탈출 가능
  if (visited[x][y] !== -1) return visited[x][y];

  visited[x][y] = 0;
  const dx = directions[pan[x][y]][0];
  const dy = directions[pan[x][y]][1];
  visited[x][y] = dfs(x + dx, y + dy);
  return visited[x][y];
}

let answer = 0
for (let n = 0; n < N; n++) {
  for (let m = 0; m < M; m++) {
    answer += dfs(n, m)
  }
}
console.log(answer)
