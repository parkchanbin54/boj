import java.io.*;
 
public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int idx = 1;
        while (true) {
 
            int N = Integer.parseInt(br.readLine());
            if (N == 0)
                break;
            
            StringBuilder sb = new StringBuilder();
 
            sb.append("Group " + idx+"\n");
 
            String list[][] = new String[N][N];
 
            for (int i = 0; i < N; i++) {
                String str[] = br.readLine().split(" ");
                list[i] = str;
            }
 
 
            int chk_R = 0;
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
 
                    if (list[i][j].equals("N")) {
 
                        chk_R = i - j;
                        if (chk_R < 0)
                            chk_R += N;
 
                        sb.append(list[chk_R][0] + " was nasty about " + list[i][0] + "\n");
                        cnt++;
                    }
                }
            }
 
            if (cnt == 0) {
                sb.append("Nobody was nasty"+"\n");
            }
            
            System.out.println(sb);
            idx++;
        }
        
        br.close();
    }
}

