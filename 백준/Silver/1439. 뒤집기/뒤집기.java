import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		
		char[] chars = str.toCharArray();
		int n = chars.length;
		int ascii = 48;
		int[] count = new int[2];	 
		char lastCh = chars[0];	
		
		for(int i = 1; i < n; i++) {
			if(lastCh != chars[i]) {
				count[lastCh - ascii]++;
				lastCh = chars[i];
			}
		}
		
		count[lastCh - ascii]++;
		
		System.out.println(Math.min(count[0], count[1]));
	}
}