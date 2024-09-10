import java.io.*;
import java.util.*;

public class Main {

    public static List<int[]> list = new ArrayList<>();
    // 금광
    public static void main(String[] args) throws Exception {
        //순차적으로 해당 위치까지 오는 최대비용 값을 갱신한다
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int tt = 0; tt < t; tt++) {
            list.add(Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray());
        }
        for (int i = 1; i < t; i++) {//수직
            for (int j = 0; j <= i; j++) {//좌우
                fillNode(i,j);
            }
        }

        int max=0;
        for (int i = 0; i < t; i++) {
            max = Math.max(max, list.get(t-1)[i]);
        }
        System.out.println(max);
    }

    public static void fillNode(int i, int j){
        int beforePrice1=0;
        int beforePrice2=0;
        if(j < list.get(i-1).length){
            beforePrice1 = list.get(i-1)[j];//위에거
        }
        if (j-1>=0) {
            beforePrice2 = list.get(i - 1)[j - 1];//
        }list.get(i)[j] = list.get(i)[j] + Math.max(beforePrice1, beforePrice2);
    }
}
