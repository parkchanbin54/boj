import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int tmp=Integer.parseInt(br.readLine());
        
        int count=0; 
        
        while(tmp>=5) {
        	count+=tmp/5;
        	tmp/=5;
        }
        System.out.println(count);
        
    }
    }