const fs = require("fs");
const stdin = (
  process.platform === "linux"
    ? fs.readFileSync("/dev/stdin").toString()
    : `10
    5 10
    6 25
    10 21
    32 43
    100 100
    50 50
    25 25
    45 67
    109 32
    128 128
`
)
  .trim()
  .split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const testCase : number = parseInt(input())
const pibo : bigint[] = Array(10001).fill(BigInt(0))
for (let tc = 0; tc < testCase; tc++) {
  const [P, Q] : number[] = input().trim().split(" ").map(Number)
  const q = BigInt(Q)
  pibo[0] = BigInt(1)
  pibo[1] = BigInt(1)
  for (let i = 2; i < P; i++) {
    if (pibo[i] === BigInt(0)) {
      pibo[i] = pibo[i-2] + pibo[i-1]
    }
  }
  console.log(`Case #${tc+1}: ${Number((pibo[P-1]%q))}`)
}


