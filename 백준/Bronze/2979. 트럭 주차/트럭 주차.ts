const fs : any  = require("fs");
const stdin : any = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `10 8 6
15 30
25 50
70 80`
)
  .trim()
  .split("\n");

const input : any = (() => {
  let line = 0;
  return (): any  => stdin[line++];
})();

const costs : number[] = input().split(" ").map(Number);
costs.unshift(0);

let answer : number = 0;
const parking : number[] = Array(101).fill(0);

for (let i : number = 0; i < 3; i++) {
  const [start, end] = input().split(" ").map(Number);
  for (let time : number = start; time < end; time++) {
    parking[time]++;
  }
}

for (const trucks of parking) {
  answer += costs[trucks] * trucks;
}
console.log(answer);