import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        
        long t=Long.parseLong(br.readLine());
        HashMap<String,Integer> Map=new HashMap<>();
        ArrayList<String> tmparr=new ArrayList<>();
        for(int i=0; i<t; i++) {
        	String tmp=br.readLine();
        	if(Map.get(tmp)==null) {
        		Map.put(tmp,1);
        		tmparr.add(tmp);
        	}
        	else {
        		Map.put(tmp, Map.get(tmp)+1);
        	}
        }
        int max=0;
        String result="";
        for(int i=0; i<tmparr.size(); i++) {
        	if(Map.get(tmparr.get(i))>max) {
        		result=tmparr.get(i);
        		max=Map.get(tmparr.get(i));
        	}
        	else if(Map.get(tmparr.get(i))==max) {
        		if(result.compareTo(tmparr.get(i))>0) {
        			result=tmparr.get(i);
        		}
        	}
        		
        }
        
        System.out.print(result);
    	}   
    }