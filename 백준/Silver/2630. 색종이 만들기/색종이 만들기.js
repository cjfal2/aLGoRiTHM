const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `8
    1 1 0 0 0 0 1 1
    1 1 0 0 0 0 1 1
    0 0 0 0 1 1 0 0
    0 0 0 0 1 1 0 0
    1 0 0 0 1 1 1 1
    0 1 0 0 1 1 1 1
    0 0 1 1 1 1 1 1
    0 0 1 1 1 1 1 1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input().trim())
const pan = Array.from(Array(N), () => input().trim().split(" ").map(Number))


function paper(p, pan2) {
  let w = 0
  let b = 0
  function recur(x, y, n) {
    let temp = 0
    for (let i = x; i < x + n; i++) {
      for (let j = y; j < y + n; j++) {
        if (pan2[i][j]) temp++
      }
    }
    if (temp === 0) {
      w++
    } else if (temp === n*n) {
      b++
    } else {
      const k = Math.round(n/2)
      recur(x, y, k)
      recur(x + k, y, k)
      recur(x, y + k, k)
      recur(x + k, y + k, k)
    }
    return
  }
  recur(0, 0, p)
  return [w, b]
}

const answer = paper(N, pan)
console.log(answer[0])
console.log(answer[1])