import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
 
public class Main {
 
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
 
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());
 
        List<Integer> list = new ArrayList<>();
        list.add(A);
 
        while (true) {
            int temp = list.get(list.size() - 1);
 
            int result = 0;
            while (temp != 0) {
                result += (int) Math.pow(temp % 10, (double) P);
                temp /= 10;
            }
 
            if (list.contains(result)) {
                int ans = list.indexOf(result);
                bw.write(ans + "\n");
                break;
            }
 
            list.add(result);
        }
 
        bw.flush();
        bw.close();
        br.close();
    }
 
}
