import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader inputOne = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer inputTwo = new StringTokenizer(inputOne.readLine());
		int n = Integer.parseInt(inputTwo.nextToken());
		long m = Long.parseLong(inputTwo.nextToken());
		inputTwo = new StringTokenizer(inputOne.readLine());
		long[] trees = new long[n];
		for (int i = 0; i < n; i++) {
			trees[i] = Integer.parseInt(inputTwo.nextToken());
		}
		long start = 0;
		long end = Arrays.stream(trees).max().getAsLong();
		long mid;
		while (start <= end) {
			mid = (start + end) / 2;
			long cnt = 0;
			for (int i = 0; i < n; i++) {
				if (trees[i] >= mid) {
					cnt += (trees[i] - mid);
				}
			}
			if (cnt >= m) {
                start = mid + 1;
			} else {
				end = mid - 1;
			}
		}
		System.out.println(end);
	}
}