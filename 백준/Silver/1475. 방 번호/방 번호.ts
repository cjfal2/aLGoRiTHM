const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `12635
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const room: string = input();
const numberList: number[] = Array(10).fill(0);

for (let i = 0; i < room.length; i++) {
  const num: number = parseInt(room[i]);
  if (num === 6 || num === 9) {
    if (numberList[6] <= numberList[9]) {
      numberList[6] += 1;
    } else {
      numberList[9] += 1;
    }
  } else {
    numberList[num] += 1;
  }
}

console.log(Math.max(...numberList));
