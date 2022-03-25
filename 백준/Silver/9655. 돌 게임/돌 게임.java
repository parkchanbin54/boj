import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());
        
        int three=t/3;
        int one=t%3;
        if((three+one)%2==0) {
            System.out.println("CY");
        }
        else {
            System.out.println("SK");
        }
    }
}