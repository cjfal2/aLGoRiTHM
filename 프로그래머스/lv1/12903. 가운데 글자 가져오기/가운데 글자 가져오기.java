class Solution {
    public String solution(String s) {
        int slen = s.length();
        if (slen == 1 || slen == 2) {
            return s;
        } 
        
        int k = slen/2;
        
        char[] chArr = s.toCharArray();
        
        
        if (slen%2 == 1) {
            char ans = chArr[k];
            return Character.toString(ans);
        } else {
            String ans1 = Character.toString(chArr[k-1]);
            String ans2 = Character.toString(chArr[k]);
            return ans1+ans2;
        }
    }
}