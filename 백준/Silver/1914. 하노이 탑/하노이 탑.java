import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static StringBuilder sb = new StringBuilder();

    public static void hanoi(int num, int from, int by, int to) {
        if(num == 1) {
            sb.append(from + " " + to + "\n");
        } else {
            hanoi(num-1, from, to, by);
            sb.append(from + " " + to + "\n");
            hanoi(num-1, by, from, to);
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        BigInteger res = new BigInteger("1");
        int N = scan.nextInt();
        if (N<=20) { 
            hanoi(N, 1, 2, 3);
            sb.insert(0, (int)(Math.pow(2, N) - 1) + "\n");
            System.out.print(sb);
        } else {
            for(int i=0; i<N; ++i) {
                res = res.multiply(new BigInteger("2")); 
            }
            res = res.subtract(new BigInteger("1")); 
            System.out.println(res);
        }
    }
}