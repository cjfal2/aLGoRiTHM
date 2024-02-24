const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `1
    2
    20 30
    40 60
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();
// 인풋 처리를 위한 코드

const t = parseInt(input().trim());
for (let i = 0; i < t; i++) {
  const p = parseInt(input().trim());
  for (let j = 0; j < p; j++) {
    const [a, b] = input().trim().split(" ").map(Number);
    console.log(a + b, a * b);
  }
}
