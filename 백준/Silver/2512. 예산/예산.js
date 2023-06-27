const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `5
    70 80 30 40 100
    450
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input());
const moneys = input().trim().split(" ").map(Number);
const ceil = parseInt(input());

let max_money = 0;
let min_money = 0;

let moneys_sum = 0;
moneys.forEach((e) => {
  moneys_sum += e;
  max_money = Math.max(max_money, e)
});

let answer = 0;
while (min_money <= max_money) {
  const middle = parseInt((min_money + max_money) / 2);
  let temp = 0;
  moneys.forEach((e) => {
   
    if (middle < e) {
      temp += middle;
    } else {
      temp += e;
    }
  });

  if (temp > ceil) {
    max_money = middle - 1;
  } else {
    answer = Math.max(answer, middle);
    min_money = middle + 1;
  }
}
console.log(answer);
