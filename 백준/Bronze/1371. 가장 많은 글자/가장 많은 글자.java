import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = "";
        
        while (true) {
            try {
                word += scanner.nextLine().replaceAll(" ", "");
            } catch (Exception e) {
                break;
            }
        }
        
        int cnt = 0;
        StringBuilder answer = new StringBuilder();
        
        for (char k = 'a'; k <= 'z'; k++) {
            int b = countOccurrences(word, k);
            if (cnt < b) {
                answer.setLength(0);
                answer.append(k);
                cnt = b;
            } else if (cnt == b) {
                answer.append(k);
            }
        }
        
        System.out.println(answer.toString());
    }
    
    public static int countOccurrences(String word, char target) {
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == target) {
                count++;
            }
        }
        return count;
    }
}
