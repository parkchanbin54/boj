import java.io.*;
import java.util.*;
public class Main{

    static Integer[] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());
        dp=new Integer[t+1];
        dp[0]=dp[1]=0;
        System.out.print(recur(t));
    }
    public static int recur(int N) {
    	if(dp[N]==null) {
    		if(N%6==0) {
    			dp[N]=Math.min(recur(N-1),Math.min(recur(N/3),recur(N/2)))+1;
    		}
    		else if(N%3==0) {
    			dp[N]=Math.min(recur(N/3),recur(N-1))+1;
    		}
    		else if(N%2==0) {
    			dp[N]=Math.min(recur(N/2),recur(N-1))+1;
    		}
    		else {
    			dp[N]=recur(N-1)+1;
    		}
    	}
    	return dp[N];
    }
}