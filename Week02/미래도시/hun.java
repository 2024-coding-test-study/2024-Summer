package 미래도시;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.io.*;
import java.util.*;

public class hun {

    public static final int INF = (int) 1e9; // 무한을 의미하는 값 (10억)

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 회사의 개수
        int M = Integer.parseInt(st.nextToken()); // 경로의 개수

        // 최단 거리 테이블을 모두 무한으로 초기화
        int[][] graph = new int[N + 1][N + 1];
        for (int i = 1; i <= N; i++) {
            Arrays.fill(graph[i], INF);
        }

        // 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
        for (int i = 1; i <= N; i++) {
            graph[i][i] = 0;
        }

        // 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        // 거쳐 갈 회사 X와 소개팅 상대 회사 K
        st = new StringTokenizer(br.readLine());
        int X = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        // 플로이드 워셜 알고리즘 수행
        for (int k = 1; k <= N; k++) {
            for (int a = 1; a <= N; a++) {
                for (int b = 1; b <= N; b++) {
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }

        // 최종적으로 1번 회사에서 K번 회사를 방문한 뒤에 X번 회사로 가는 최단 거리
        int distance = graph[1][K] + graph[K][X];

        // 도달할 수 없는 경우, -1을 출력
        if (distance >= INF) {
            System.out.println(-1);
        } else {
            System.out.println(distance);
        }
    }
}
