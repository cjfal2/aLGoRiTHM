const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `3 1
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();



let [N, K] = input().split(" ").map(Number);
let answer = 0;
while (true) {
  let cnt = 0;
  let temp = N;

  while (temp > 0) {
    cnt += (temp % 2)
    temp = Math.floor(temp / 2)
  }
  
  if(cnt <= K) {
    console.log(answer)
    break
  }
  answer += 1
  N += 1
}

