import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int front = 0;
        int next = 0;
        int[] n = Arrays.stream(br.readLine().split(""))
                .mapToInt(Integer::parseInt)
                .toArray();
        for(int i =0; i<n.length/2;i++){
            front += n[i];
        }
        for(int i =0; i<n.length/2;i++){
            next += n[n.length-i-1];
        }System.out.println(next==front?"LUCKY":"READY");

    }
}