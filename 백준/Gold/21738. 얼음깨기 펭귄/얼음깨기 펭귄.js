const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `21 6 12
    1 9
    1 10
    10 12
    2 13
    13 11
    11 12
    3 8
    8 7
    8 12
    5 19
    5 14
    14 12
    6 20
    6 21
    20 15
    15 12
    4 18
    4 17
    17 16
    16 12
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, S, P] = input().trim().split(" ").map(Number);
const G = Array.from(Array(N + 1), () => Array());

for (let i = 0; i < N - 1; i++) {
  const [from, to] = input().trim().split(" ").map(Number);
  G[from].push(to);
  G[to].push(from);
}

const visited = Array(N + 1).fill(0);
const temp = [];

for (let i = 1; i < S+1; i++) {
  const queue = [[i, 0]];
  visited[i] = 1;
  while (queue.length > 0) {
    const [node, count] = queue.shift();
    G[node].forEach((element) => {
      if (visited[element] === 0) {
        if (element === P) {
          temp.push(count + 1);
        } else {
          queue.push([element, count + 1]);
          visited[element] = 1;
        }
      }
    });
  }
}
temp.sort((a, b) => a - b);
console.log(N - temp[0] - temp[1] - 1);
