import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		Scanner scanner = new Scanner(System.in);  // 난 scanner를 통해서 인풋을 받을거다.
		int n = scanner.nextInt();
		int ans = 0;

		for (int i = 0; i < n; i++) {
			ans += scanner.nextInt();
		}

		System.out.println(ans);
	}
}