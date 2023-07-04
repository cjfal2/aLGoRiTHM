const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `8 2
    0 1
    0 2
    1 3
    1 4
    2 5
    2 6
    6 7
    1 0 0 1 0 1 0 1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [n, k] = input().trim().split(" ").map(Number);
const tree = Array.from(Array(n), () => Array());

for (let i = 0; i < n - 1; i++) {
  const [from, to] = input().trim().split(" ").map(Number);
  tree[from].push(to);
}

const appleInformation = input().trim().split(" ").map(Number);
let answer = 0;

function dfs(node, depth, tree) {
  answer += appleInformation[node];
  if (depth === k) return;

  tree[node].forEach(element => {
    dfs(element, depth + 1, tree);
  });
}

dfs(0, 0, tree);
console.log(answer);
