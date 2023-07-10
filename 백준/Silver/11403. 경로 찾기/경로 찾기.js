const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `7
    0 0 0 1 0 0 0
    0 0 0 0 0 0 1
    0 0 0 0 0 0 0
    0 0 0 0 1 1 0
    1 0 0 0 0 0 0
    0 0 0 0 0 0 1
    0 0 1 0 0 0 0
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input().trim());
const G = Array.from(Array(N), () => Array());

for (let k = 0; k < N; k++) {
  const inputArray = input().trim().split(" ").map(Number);
  for (let p = 0; p < N; p++) {
    if (inputArray[p] === 1) {
      G[k].push(p);
    }
  }
}

const answer = Array.from(Array(N), () => Array(N).fill(0));

for (let i = 0; i < N; i++) {
  for (let j = 0; j < N; j++) {
    const visited = Array(N).fill(0);
    dfs(i, i, j, 0, visited);
  }
}

answer.forEach((v) => {
  console.log(v.join(" "));
});

function dfs(first, x, y, depth, visited) {
  if (x === y && depth > 0) {
    answer[first][y] = 1;
    return;
  }

  if (first !== x) {
    visited[x] = 1;
  }

  G[x].forEach((w) => {
    if (!visited[w]) {
      dfs(first, w, y, depth + 1, visited);
    }
  });
}
