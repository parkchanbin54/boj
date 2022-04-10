import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String tmp=br.readLine();
        int t=tmp.length();
        int[] arr=new int[t];
        for(int i=0; i<t; i++){
            arr[i]=Character.getNumericValue(tmp.charAt(i));
        }
        Arrays.sort(arr);
        for(int i=t-1; i>=0; i--){
            System.out.print(arr[i]);
        }
    }
}