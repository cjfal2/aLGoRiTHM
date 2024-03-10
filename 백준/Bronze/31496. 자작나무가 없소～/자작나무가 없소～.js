const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `2 stone
    stone 64
    cobblestone 32
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, target] = input().trim().split(" ")
const n = parseInt(N)
let answer = 0
for (let i = 0; i < n; i++) {
  const [word, number] = input().trim().split(" ")
  const num = parseInt(number)
  const sepWord = word.split("_")
  if (sepWord.includes(target)) {
    answer = answer + num
  }
}
console.log(answer)