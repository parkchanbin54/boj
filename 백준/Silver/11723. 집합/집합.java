import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t=Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuffer sb=new StringBuffer();
        int[] S=new int[21];
        for(int i=0; i<S.length; i++)
        	S[i]=0;
        for(int i=0; i<t; i++) {
        	st=new StringTokenizer(br.readLine());
        	String tmp=st.nextToken();
        	if(tmp.compareTo("add")==0) {
        		S[Integer.parseInt(st.nextToken())]=1;
        	}
        	else if(tmp.compareTo("check")==0) {
        		if(S[Integer.parseInt(st.nextToken())]==1)
        			sb.append(1).append('\n');
        		else
        			sb.append(0).append('\n');
        	}
        	else if(tmp.compareTo("remove")==0) {
        		
        		S[Integer.parseInt(st.nextToken())]=0;
        	}
        	else if(tmp.compareTo("toggle")==0) {
        		int tmp2=Integer.parseInt(st.nextToken());
        		if(S[(tmp2)]==0)
        			S[(tmp2)]=1;
        		else
        			S[(tmp2)]=0;        			        		
        	}
        	else if(tmp.compareTo("all")==0) {
        		for(int j=0; j<S.length; j++)
                	S[j]=1;	       			        		
        	}
        	else if(tmp.compareTo("empty")==0) {
        		for(int j=0; j<S.length; j++)
                	S[j]=0;	       			        		
        	}
        }
        System.out.print(sb);
    }
}