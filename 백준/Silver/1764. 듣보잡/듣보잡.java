import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        int max=0;
        if(N>M)
        	max=N;
        else
        	max=M;
        HashMap<String,Integer> Map=new HashMap<String,Integer>();
        ArrayList<String> answer=new ArrayList<>();
        
        for(int i=0; i<N; i++) {
        	String tmp=br.readLine();
        	Map.put(tmp, 0); 	
        }
        
        for(int i=0; i<M; i++) {
        	String tmp=br.readLine();
        	if(Map.get(tmp)!=null) {
        		answer.add(tmp+"\n");
        	}
        }
        
        Collections.sort(answer);
        
        System.out.println(answer.size());
        for(int i=0; i<answer.size(); i++)
        	System.out.print(answer.get(i));
        
        
    	}
    }