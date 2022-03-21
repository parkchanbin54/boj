import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int k=Integer.parseInt(br.readLine());
        boolean flag=false;
        for(int i=k/2; i<k; i++){
            String tmp=String.valueOf(i);
            int total=0;
            for(int j=0; j<tmp.length(); j++){
                total+=Character.getNumericValue(tmp.charAt(j));
            }
            if(total+i==k){
                System.out.print(i);
                flag=true;
                break;
            }
        }
        if(!flag)
            System.out.print(0);
    }
}