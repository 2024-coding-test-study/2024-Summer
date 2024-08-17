import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int[] NMKX; // 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
    public static List<List<Integer>> road = new ArrayList<>();
    public static int[] minLengthToX;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        NMKX = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int N = NMKX[0];
        int M = NMKX[1];
        int K = NMKX[2];
        int X = NMKX[3] - 1;

        for (int i = 0; i < N; i++) {
            road.add(new ArrayList<>());
        }

        for (int i = 0; i < M; i++) {
            int[] tmp = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            road.get(tmp[0] - 1).add(tmp[1] - 1); // 1-based index to 0-based index
        }

        minLengthToX = new int[N];
        Arrays.fill(minLengthToX, Integer.MAX_VALUE);
        minLengthToX[X] = 0;

        dijkstra(X);

        boolean found = false;
        for (int i = 0; i < N; i++) {
            if (minLengthToX[i] == K) {
                System.out.println(i + 1); // 0-based index to 1-based index
                found = true;
            }
        }

        if (!found) {
            System.out.println(-1);
        }
    }

    public static void dijkstra(int start) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Comparator.comparingInt(node -> minLengthToX[node]));
        queue.add(start);

        while (!queue.isEmpty()) {
            int idx = queue.poll();

            for (int e : road.get(idx)) {
                if (minLengthToX[e] > minLengthToX[idx] + 1) {
                    minLengthToX[e] = minLengthToX[idx] + 1;
                    queue.add(e);
                }
            }
        }
    }
}
