const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1
    2
    0 0
    1000 5
    2000 10
    3000 15
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

function bfs(home, visited, festival, store, N) {
  const queue = [[home[0], home[1]]];
  while (queue.length > 0) {
    const [x, y] = queue.shift();
    if (Math.abs(x - festival[0]) + Math.abs(y - festival[1]) <= 1000) {
      console.log("happy");
      return;
    }
    for (let j = 0; j < N; j++) {
      if (!visited[j]) {
        const [nx, ny] = store[j];
        if (Math.abs(x - nx) + Math.abs(y - ny) <= 1000) {
          queue.push([nx, ny]);
          visited[j] = 1;
        }
      }
    }
  }
  console.log("sad");
}

const testCase = parseInt(input().trim());
for (let tc = 0; tc < testCase; tc++) {
  const N = parseInt(input().trim());
  const home = input().trim().split(" ").map(Number);
  const store = [];
  for (let i = 0; i < N; i++) {
    const [x, y] = input().trim().split(" ").map(Number);
    store.push([x, y]);
  }
  const festival = input().trim().split(" ").map(Number);
  const visited = Array(N + 1).fill(0);
  bfs(home, visited, festival, store, N);
}
