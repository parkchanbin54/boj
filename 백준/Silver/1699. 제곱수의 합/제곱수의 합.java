import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static int d[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        d = new int[number+1];
        //d[n] = min(d[n - i^2] + 1)
        for (int i = 1; i <= number; i++){
            d[i] = i;
            for (int j = 1; j*j <= i; j++){
                if (d[i] > d[i-j*j]+1){
                    d[i] = d[i-j*j]+1;
                }
            }
        }
        System.out.println(d[number]);
    }
}