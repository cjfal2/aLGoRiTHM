const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `428392
    17
`
).split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

let N = input()
const F = input()
const slicedNumber = N.substring(0, N.length-2)
let temp = slicedNumber + "00"

while (true) {
  if (temp%F === 0) {
    console.log(temp.toString().substring(N.length-2, N.length+1))
    break
  } else {
    temp ++
  }
}