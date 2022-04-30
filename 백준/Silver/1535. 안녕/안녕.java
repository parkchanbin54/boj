import java.io.*;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] energy = new int[n+1];
		for(int i=1; i<n+1; i++) {
			energy[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		int[] gift = new int[n+1];
		for(int i=1; i<n+1; i++) {
			gift[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] dp = new int[101];
        
		for(int i=1; i<n+1; i++) {
			for(int j=99; j>=0; j--) {
				int ene = energy[i]+j;
				if(ene<100) {
					dp[ene] = Math.max(dp[ene], dp[j]+gift[i]);
				}
			}
		}
		System.out.println(dp[99]);
		
	}
}