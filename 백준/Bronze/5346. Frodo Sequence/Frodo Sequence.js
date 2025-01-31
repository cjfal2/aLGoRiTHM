const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `2
4
5
6
0`
)
  .trim()
  .split("\n")
  .map(Number);

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

function frodoSequence(n) {
  if (n === 1 || n === 2) return 1;
  if (n === 3) return 2;

  let fro1 = 1, fro2 = 1, fro3 = 2, froN;
  for (let i = 4; i <= n; i++) {
    froN = fro3 + fro2 - fro1;
    fro1 = fro2;
    fro2 = fro3;
    fro3 = froN;
  }
  return froN;
}

while (true) {
  const n = input();
  if (n === 0) break;
  console.log(frodoSequence(n));
}
