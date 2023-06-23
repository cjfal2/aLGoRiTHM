const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `2 2
    500
    501
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const [N, M] = input().trim().split(" ").map(Number);
const moneys = [];

let min_money = 10000000;
let max_money = 0;
let sum = 0;

for (let i = 0; i < N; i++) {
  const temp = parseInt(input());
  min_money = Math.min(temp, min_money);
  max_money = Math.max(temp, max_money);
  sum += temp;
  moneys.push(temp);
}

let answer = 0;
let left = min_money;
let right = sum;

while (left <= right) {
  const middle = parseInt((left + right) / 2); // 인출 금액
  let total = 0;
  let count = 0; // 인출 횟수
  moneys.forEach((money) => {
    //리스트 순회
    if (total < money) {
      // 돈 보다 total이 적으면 total값을 mid로 설정을 하고 카운트를 센다.
      total = middle;
      count++;
    }
    total -= money; // total값에서 돈만큼 뺀다.
  });

  if (count > M || max_money > middle) {
    // 인출 횟수가 원하는 숫자를 넘었거나 middle이 최대 돈보다 작으면 왼쪽을 끌어와 큰쪽에서 범위 탐색을 한다.
    left = middle + 1;
  } else {
    right = middle - 1;
    answer = middle;
  }
}
console.log(answer);
