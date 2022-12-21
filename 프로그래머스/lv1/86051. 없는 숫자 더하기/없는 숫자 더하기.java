class Solution {
    public int solution(int[] numbers) {
        
        int answer = 0;
        for (int i = 0; i<10; i++) {
            boolean flag = true;
            for (int num : numbers) {
                if (i == num) {
                    flag = false;
                    break;
                }
            };
            if (flag) {
              answer += i;
            };
        };
        
        
        return answer;
    }
}