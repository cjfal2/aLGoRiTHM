const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `6
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
let bunja = N;
let bunmo = 24;

for (let i = 3; i !== 0; i--) {
  bunja *= (N - i)
}
console.log(Math.floor(bunja/bunmo))