function solution(n)
{
    let answer = 0;
    
    const newNumber = n.toString();
    
    for (let i = 0; i < newNumber.length; i++) {
        answer = answer + parseInt(newNumber[i]);
    }

    return answer;
}