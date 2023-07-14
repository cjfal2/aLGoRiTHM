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

const [N, P, Q, X, Y] = input().split(" ").map(Number);
const answer = {"0": 1};

function infinite(N) {
  if (N < 0) return 1;

  if (N in answer) return answer[N];

  answer[N] = infinite(Math.floor(N / P) - X) + infinite(Math.floor(N / Q) - Y);
  return answer[N]
}

console.log(infinite(N));
