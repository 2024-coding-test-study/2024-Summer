import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
class Main{//병사 배치하기
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] list  = new int[n];
        for (int i = 0; i < n; i++) {
            list[i] = Integer.parseInt(br.readLine());
        }
        int[] list2 = new int[n];
        for (int i = 0; i < n; i++) {
            list2[n-1-i] = list[i];
        }

        //최장증가부분수열을 이용해야 함
        //해당 값을 마지막 노드로 하는 부분 수열의 최대길이
        int[] dp = new int[n];
        Arrays.fill(dp,1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                //이전 노드중 자신보다 작은 dp값 중 가장 큰 값
                if(list2[i]>list2[j]) dp[i]=Math.max(dp[i],dp[j]+1);
            }
            System.out.println(dp[i]);
        }

        int max = 0;
        for(int dpEntity: dp){
            if (max<dpEntity) max = dpEntity;
        }
        System.out.println(max);




    }
}
