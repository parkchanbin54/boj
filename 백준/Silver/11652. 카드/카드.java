import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        
        long t=Long.parseLong(br.readLine());
        HashMap<Long,Integer> Map=new HashMap<>();
        ArrayList<Long> tm=new ArrayList<>();
        for(int i=0; i<t; i++) {
        	long tmp=Long.parseLong(br.readLine());
        	if(Map.get(tmp)==null) {
        		Map.put(tmp,1);
        		tm.add(tmp);
        	}        	
        	else {
        		Map.put(tmp, Map.get(tmp)+1);		
        	}
        }
        
        int max=0;
        long result=0;
        
        for(int i=0; i<tm.size(); i++) {
        	if(Map.get(tm.get(i))>max) {
        		max=Map.get(tm.get(i));
        		result=tm.get(i);
        	}
        	else if(Map.get(tm.get(i))==max) {
        		if(result>tm.get(i))
        			result=tm.get(i);        		
        	}
        }
        
        System.out.println(result);
        
        
    	}   
    }