import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        List<Integer> list = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            list.add(i);
        }

        while (list.size() > 1) {
            list.remove(0); // 첫 번째 카드를 버린다.
            list.add(list.remove(0)); // 두 번째 카드를 끝으로 이동시킨다.
        }

        System.out.println(list.get(0)); // 마지막으로 남은 카드 출력
    }
}
