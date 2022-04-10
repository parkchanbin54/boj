import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
	static int map[][];
	static int tmp[];
	static int res, mx, N;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		map = new int [N][5];
		tmp = new int [N];
		StringTokenizer st;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < 5; j++) {
				for (int k = j + 1; k < 5; k++) {
					for (int l = k + 1; l < 5; l++) {
						tmp[i] = Math.max(tmp[i], 
								(map[i][j] + map[i][k] + map[i][l]) % 10);
					}
				}
			}
			mx = Math.max(tmp[i], mx);
		}
		
		for (int i = 0; i < N; i++) {
			if(tmp[i] == mx) {
				res = i + 1;
			}
		}
		System.out.println(res);
	}
}