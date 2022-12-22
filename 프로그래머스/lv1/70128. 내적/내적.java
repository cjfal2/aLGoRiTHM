class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for (int i = 0; i < a.length; i++) {
            int aa = a[i];
            int bb = b[i];
            int cc = aa*bb;
            answer += cc;
        }
        return answer;
    }
}