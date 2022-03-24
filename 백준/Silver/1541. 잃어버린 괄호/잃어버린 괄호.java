import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String tmp=br.readLine();
        int count=0;
        ArrayList<Integer> digits=new ArrayList<>();
        ArrayList<String> para=new ArrayList<>();
        String store="0";
        for(int i=0; i<tmp.length(); i++) {
        	if(isdigit(tmp.substring(i,i+1))) {
        		store=store.concat(tmp.substring(i,i+1));
        	}
        	else {
        		digits.add(Integer.parseInt(store));
        		store="0";
        		para.add(tmp.substring(i,i+1));
        	}	
        }
        digits.add(Integer.parseInt(store));
        
        int sum=0;
        int result=digits.get(0);
        boolean check=false;
        
        for(int i=0; i<para.size(); i++) {
        	if(para.get(i).compareTo("-")==0) {
        		result-=digits.get(i+1);
        		if(!check) {
        			check=true;
        		}
        	}
        	else if(para.get(i).compareTo("+")==0){
        		if(check)
        			result-=digits.get(i+1);
        		else
        			result+=digits.get(i+1);
        	}
        	
        }
        
        if(sum!=0&&!check)
        	result+=sum;
        else if(sum!=0&&check)
        	result-=sum;
        
        System.out.println(result);
        		
    }
    public static boolean isdigit(String c) {
    	try {
    		Integer.parseInt(c);
    	}
    	catch(NumberFormatException e) {
    		return false;
    	}
    	return true;
    }
    }