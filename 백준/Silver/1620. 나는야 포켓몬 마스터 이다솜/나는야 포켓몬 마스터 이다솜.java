import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        
        HashMap<String, Integer> nameMap=new HashMap<String, Integer>();
        String[] nameArr=new String[N+1];
        
        for(int i=1; i<N+1; i++) {
        	String tmp=br.readLine();
        	nameMap.put(tmp, i);
        	nameArr[i]=tmp;
        }
        
        StringBuilder sb=new StringBuilder();
        
        for(int i=0; i<M; i++) {
        	String tmp=br.readLine();
        	if(isString(tmp)) {
        		sb.append(nameArr[Integer.parseInt(tmp)]);
        	}
        	else {
        		sb.append(nameMap.get(tmp));
        	}
        	sb.append('\n');
        }
        System.out.print(sb);
        
        
    }
    public static boolean isString(String tmp) {
    	try {
    		Double.parseDouble(tmp);
    		return true;
    	}
    	catch(NumberFormatException e){
    		return false;
    	}
    }
}