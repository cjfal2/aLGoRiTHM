function solution(n, s) {
  var answer = [];
  if (parseInt(s/n) === 0) {
    return [-1]
  }

  while (true) {
    let num = parseInt(s/n)
    answer.push(num)
    s -= num
    n -= 1
    if (n === 0) {
      return answer
    }
  }

  return answer;
}