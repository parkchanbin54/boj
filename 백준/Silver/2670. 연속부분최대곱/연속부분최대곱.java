import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		

		int n = Integer.parseInt(br.readLine());
		double[] arr = new double[n];
		for(int i = 0; i < n; i++) {
			arr[i] = stod(br.readLine());
		}
		
		double max = arr[0];
		

		for(int i = 1; i < n; i++) {
			arr[i] = Math.max(arr[i], arr[i-1] * arr[i]);
			max = Math.max(max, arr[i]);
		}
		System.out.printf("%.3f", max);
	}
	public static double stod(String str) {return Double.parseDouble(str);}
}