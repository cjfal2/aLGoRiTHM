function solution(s){
  const aa = [...s]
  let ps = 0
  let ys = 0
  aa.forEach(element => {
    if (element === 'p' || element === 'P') {
      ps ++
    } else if (element === 'y' || element === 'Y') {
      ys ++
    }
  });
  if (ps === ys) {
    var answer = true
  } else {
    var answer = false
  }
  return answer;
}