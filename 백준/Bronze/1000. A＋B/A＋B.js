//한 줄의 입력(띄어쓰기 o , 예를 들면 1 2 3 4 5)
function solution(input){
    const [a,b] = input;
    const answer = a+b;
    console.log(answer);
}

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input;
let list = [];
rl.on('line', function(line) {
    input = line;
    rl.close();
}).on("close", function() {
    // list = input.split(' ').map((el) => el); 
    list = input.split(' ').map((el) => parseInt(el)); // 입력값이 정수라면 parseInt로 형 변환
    solution(list);
    process.exit();
});