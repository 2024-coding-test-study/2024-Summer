import java.util.ArrayList;
import java.util.List;

class Solution {
    static List<List<Integer>> map;

    public int solution(int n, int[][] wires) {
        map = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            map.add(new ArrayList<>());
        }

        // 무향 그래프를 구성
        for (int i = 0; i < wires.length; i++) {
            int v1 = wires[i][0] - 1;  // 0-based index
            int v2 = wires[i][1] - 1;  // 0-based index
            map.get(v1).add(v2);
            map.get(v2).add(v1);
        }

        int minDifference = Integer.MAX_VALUE;

        // 각 간선을 하나씩 끊어보며 최소 차이를 계산
        for (int i = 0; i < wires.length; i++) {
            int v1 = wires[i][0] - 1;
            int v2 = wires[i][1] - 1;

            // 간선을 끊음
            map.get(v1).remove(Integer.valueOf(v2));
            map.get(v2).remove(Integer.valueOf(v1));

            // 방문 배열 초기화 및 연결된 송전탑의 수 계산
            boolean[] visited = new boolean[n];
            int count = countLinked(v1, visited);

            // 현재 끊어진 경우의 차이 계산
            int difference = Math.abs(n - 2 * count);
            minDifference = Math.min(minDifference, difference);

            // 간선 복구
            map.get(v1).add(v2);
            map.get(v2).add(v1);
        }

        return minDifference;
    }

    public static int countLinked(int v, boolean[] visited) {
        // 연결된 송전탑 수를 계산하는 함수
        if (visited[v]) return 0;
        visited[v] = true;

        int count = 1;
        for (int neighbor : map.get(v)) {
            count += countLinked(neighbor, visited);
        }
        return count;
    }
}
