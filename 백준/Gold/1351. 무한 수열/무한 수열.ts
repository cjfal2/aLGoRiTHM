const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `7 2 3
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, P, Q] = input().split(" ").map(Number);
const answer = {"0": 1};

function infinite(N) {
  if (N in answer) return answer[N];

  answer[N] = infinite(Math.floor(N / P)) + infinite(Math.floor(N / Q));
  return answer[N]
}

console.log(infinite(N));
