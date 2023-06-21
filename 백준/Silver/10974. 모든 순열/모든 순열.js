const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3
`
).trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
let stack = [];

function back() {
  if (stack.length === N) {
    console.log(stack.join(" "))
    return
  }
  for (let i = 1; i < N+1; i++) {
    if (!stack.includes(i)) {
      stack.push(i)
      back()
      stack.pop()
    }
  }
}
back()
