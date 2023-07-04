const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `8 5
    0 1
    0 2
    1 3
    1 4
    2 5
    2 6
    6 7
    0 1 2 3 4 5 6 7
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
  tree[to].push(from)
};

tree[0] = -1

let target = 0;
const inputInformation = input().trim().split(" ").map(Number);

for (let j = 0; j < n; j++) {
  if (inputInformation[j] === k) {
    target = j
    break
  }
}

function depthToRoot(node, depth, tree) {
  if (tree[node] === -1) return depth;
  
  return depthToRoot(tree[node], depth + 1, tree);
}

console.log(depthToRoot(target, 0, tree))