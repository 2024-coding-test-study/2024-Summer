import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] ns = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int n = ns[0];
        int s = ns[1];

        int[] nList = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int start = 0;
        int end = 0;
        int min = Integer.MAX_VALUE;
        int sum = 0;

        //슬라이딩 윈도우기법
        //end의 값 하나씩 올리고 start의 값 내릴 수 있는 만큼 계속 내림
        while (end < n) {
            sum += nList[end++];

            while (sum >= s) {
                min = Math.min(min, end - start);
                sum -= nList[start++];
            }
        }

        System.out.println(min == Integer.MAX_VALUE ? 0 : min);
    }
}
