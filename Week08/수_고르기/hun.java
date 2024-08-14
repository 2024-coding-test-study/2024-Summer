import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {


        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int n = nm[0];
        int m = nm[1];

        int[] nList = new int[n];
        for (int i = 0; i < n; i++) {
            nList[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(nList);
        if(nList.length<=1){
            if(m==0) System.out.println(0);
            else System.out.println(-1);
            return;
        }
        int start = 0;
        int end = 1;
        int min = Integer.MAX_VALUE;
        while (end < nList.length){
            int gap = nList[end] - nList[start];
            if (gap < m){
                end++;
            }else {
                if(m==gap){
                    System.out.println(m);
                    return;
                }
                min = Math.min(gap,min);
                start++;
            }
        }
        if (min!= Integer.MAX_VALUE) System.out.println(min);
        else System.out.println(-1);
        bw.flush();
    }
}
