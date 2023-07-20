const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `30
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    1
    2
    2
    2
    2
    2
    2
    2
    2
    2
    4
    4
    4
    4
    4
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input().trim());

if (N === 0) {
  console.log(0);
} else {
  const percents = Math.round(N * 0.15);

  const scores = Array(N).fill(0);
  for (let i = 0; i < N; i++) {
    const a = parseInt(input().trim());
    scores[i] = a;
  }
  scores.sort((a, b) => a - b);

  let sum = 0;

  for (let j = percents; j + percents < N; j++) {
    sum += scores[j];
  }

  console.log(Math.round(sum / (N - percents * 2)));
}
