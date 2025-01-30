const fs = require("fs");
const stdin = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const input = (() => {
  let line = 0;
  return () => stdin[line++];
})();

const N = parseInt(input().trim());


for (let i = 0; i < N; i++) {
  const [id, s1, s2, s3] = input().trim().split(" ").map(Number);
  
  const total = s1 + s2 + s3;
  const minS1 = 35 * 0.3;
  const minS2 = 25 * 0.3;
  const minS3 = 40 * 0.3;

  const pass = total >= 55 && s1 >= minS1 && s2 >= minS2 && s3 >= minS3 ? "PASS" : "FAIL";
  
  console.log(`${id} ${total} ${pass}`);
}
