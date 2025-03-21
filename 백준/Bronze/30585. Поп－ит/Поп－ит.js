const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `2 3
010
001`
).trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [h, w] = input().split(" ").map(Number);
let count0 = 0;
let count1 = 0;

for (let i = 0; i < h; i++) {
  const row = input().trim();
  for (let ch of row) {
    if (ch === '0') count0++;
    else count1++;
  }
}

console.log(Math.min(count0, count1));
