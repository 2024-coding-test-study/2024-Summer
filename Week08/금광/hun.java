import java.io.*;
import java.util.*;

public class Main {
    public static int[][] list2;
    // 금광
    public static void main(String[] args) throws Exception {
        //순차적으로 해당 위치까지 오는 최대비용 값을 갱신한다
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int tt = 0; tt < t; tt++) {
            // m과 n을 한 번에 가져오고, 배열 생성
            String[] mnInput = br.readLine().split(" ");
            int n = Integer.parseInt(mnInput[0]);
            int m = Integer.parseInt(mnInput[1]);
            list2 = new int[n][m];

            // 입력받은 데이터를 m * n 크기의 2차원 배열로 변환
            int[] list1 = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            // 1차원 배열을 2차원 배열로 변환
            for (int i = 0; i < n; i++) {
                System.arraycopy(list1, i * m, list2[i], 0, m);
            }
            for (int i = 1; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    fillNode(i,j,n);

                }
            }
            int max=0;
            for (int i = 0; i < n; i++) {
                max = Math.max(max, list2[i][m-1]);
            }
            System.out.println(max);
        }




    }
    public static void fillNode(int x, int y, int n){
        int beforePrice1=0;
        int beforePrice2=0;
        int beforePrice3=0;

        if (y-1>=0){
            beforePrice1 = list2[y-1][x-1];
        }if (y+1<n){
            beforePrice2 = list2[y+1][x-1];
        }beforePrice3 = list2[y][x-1];

        int max=beforePrice1>beforePrice2?beforePrice1:beforePrice2;
        max = max> beforePrice3?max:beforePrice3;
        list2[y][x] = list2[y][x]+ max;
    }
}
