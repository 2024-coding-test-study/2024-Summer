import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        //끝나는 시간 기준 정렬
        //해당 노드보다 크다면 count++;

        List<int[]> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            list.add(Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray());
        }

        //list.sort(Comparator.comparingInt(o -> o[1]));
        //시작시간과 끝나는 시간이 같은 케이스를 고려해야함
        list.sort((o1, o2) -> {
            if (o1[1] == o2[1]) {
                return o1[0] - o2[0];  // 끝나는 시간이 같다면 시작 시간이 빠른 회의 우선
            }
            return o1[1] - o2[1];  // 끝나는 시간 기준으로 오름차순 정렬
        });

        int count=0;
        int lastEndTime=0;
        for (int i = 0; i < n; i++) {
            if(lastEndTime<=list.get(i)[0]){
                count++;
                lastEndTime = list.get(i)[1];
            }

        }
        System.out.println(count);
    }
}
