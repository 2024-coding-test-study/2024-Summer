import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int v = Integer.parseInt(st.nextToken()); // 정점의 수
        int e = Integer.parseInt(st.nextToken()); // 간선의 수
        int start = Integer.parseInt(br.readLine()) - 1; // 시작 정점 (0부터 시작하도록 -1)

        List<int[]>[] adj = new ArrayList[v];
        for (int i = 0; i < v; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken()) - 1;
            int w = Integer.parseInt(st.nextToken()) - 1;
            int weight = Integer.parseInt(st.nextToken());
            adj[u].add(new int[] {w, weight});
        }

        int[] distance = new int[v];
        Arrays.fill(distance, Integer.MAX_VALUE);
        distance[start] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[1]));
        pq.add(new int[] {start, 0});

        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int currNode = curr[0];
            int currDist = curr[1];

            if (currDist > distance[currNode]) continue;

            for (int[] edge : adj[currNode]) {
                int nextNode = edge[0];
                int nextDist = currDist + edge[1];

                if (nextDist < distance[nextNode]) {
                    distance[nextNode] = nextDist;
                    pq.add(new int[] {nextNode, nextDist});
                }
            }
        }

        for (int i = 0; i < v; i++) {
            if (distance[i] == Integer.MAX_VALUE) {
                System.out.println("INF");
            } else {
                System.out.println(distance[i]);
            }
        }
    }
}
