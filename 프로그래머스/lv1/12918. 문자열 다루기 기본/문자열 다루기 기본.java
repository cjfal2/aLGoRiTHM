class Solution {
    public boolean solution(String s) {
        String[] ss = s.split("");
        String n = "0123456789";
        String[] nums = n.split("");
        int aa = s.length();
        if (aa == 4 || aa == 6) {
            for (int i = 0; i < aa; i++) {
                boolean flag = false;
                for (String what : nums) {
                    if (what.equals(ss[i])) {
                        flag = true;
                        break;
                    }
                }
                if (!flag) {
                    return false;
                }
            }
            return true;
            
        } else {
            return false;    
        }
    }
}