import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

	
	static boolean visit[];
	static int count;
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int num = Integer.parseInt(br.readLine());
		Integer arr[] = new Integer[num];
		long result = 0;
		for(int i=0; i<num; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		Arrays.sort(arr,Collections.reverseOrder());
		for(int i=0; i<num; i++) {
			int count = arr[i] - (i+1-1);
			if(count > 0) {
				result += count;
			}
			else {
				continue;
			}
		}
		bw.write(String.valueOf(result));
		
		bw.flush();
		bw.close();
	}
}