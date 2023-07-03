const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3 2
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [n, m] = input().trim().split(" ").map(Number);

for (let node = 0; node < n - m + 1; node++) {
  console.log(node, node + 1);
}

if (m > 2)
  for (let node = n - m + 2; node < n; node++) {
    console.log(n - m, node);
  }
