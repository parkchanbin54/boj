import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int t=Integer.parseInt(br.readLine());
        
        for(int i=0; i<t; i++) {
        	int amount=Integer.parseInt(br.readLine());
        	HashMap<String,Integer> tmpMap=new HashMap<>();
        	ArrayList<String> var=new ArrayList<String>();
        	for(int j=0; j<amount; j++) {
        		st=new StringTokenizer(br.readLine());
        		String a=st.nextToken();
        		String b=st.nextToken();
        		if(tmpMap.get(b)!=null) {
        			tmpMap.put(b,tmpMap.get(b)+1);
        		}
        		else {
        			tmpMap.put(b,1);
        			var.add(b);
        		}
        			
        	}
        	int result=1;
        	for(int j=0; j<var.size(); j++) {
        		result*=(tmpMap.get(var.get(j))+1);
        	}
        	System.out.println(result-1);
        }
        
    	}

    
    }