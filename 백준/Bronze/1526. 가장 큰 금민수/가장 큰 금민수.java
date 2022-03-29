import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();

		for(int i=N; i>=4; i--) {
			boolean flag = true;
			int num = i;
			while(num != 0) {
				if(num % 10 == 4 || num % 10 == 7)
					num /= 10;
				else {
					flag = false;
					break;
				}
			}
			
			if(flag) {
				System.out.println(i);
				break;
			}
		}
		scan.close();
	}

}