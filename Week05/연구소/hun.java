import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int N;
    public static int M;
    public static int maxSafeArea = 0;
    public static int[][] map;
    public static int[][] tempMap;
    public static List<Pos> virus = new ArrayList<>();

    public static int[] dx = {1, -1, 0, 0};
    public static int[] dy = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] NM = br.readLine().split(" ");
        N = Integer.parseInt(NM[0]);
        M = Integer.parseInt(NM[1]);

        map = new int[N][M];
        tempMap = new int[N][M];

        for (int i = 0; i < N; i++) {
            String[] row = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(row[j]);
                if (map[i][j] == 2) {
                    virus.add(new Pos(i, j));
                }
            }
        }

        makeWall(0);
        System.out.println(maxSafeArea);
    }

    public static void makeWall(int wallCount) {
        if (wallCount == 3) {
            spreadVirus();
            maxSafeArea = Math.max(maxSafeArea, countSafeArea());
            return;
        }

        for (int i = 0; i < N * M; i++) {
            int x = i / M;
            int y = i % M;
            if (map[x][y] == 0) {
                map[x][y] = 1;
                makeWall(wallCount + 1);
                map[x][y] = 0;
            }
        }
    }

    public static void spreadVirus() {
        for (int i = 0; i < N; i++) {
            System.arraycopy(map[i], 0, tempMap[i], 0, M);
        }

        Queue<Pos> queue = new LinkedList<>();
        for (Pos v : virus) {
            queue.add(v);
        }
        //얼음얼려먹기와 같이 BFS활용
        while (!queue.isEmpty()) {
            Pos pos = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = pos.x + dx[i];
                int ny = pos.y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    if (tempMap[nx][ny] == 0) {
                        tempMap[nx][ny] = 2;
                        queue.add(new Pos(nx, ny));
                    }
                }
            }
        }
    }

    public static int countSafeArea() {
        int safeCount = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (tempMap[i][j] == 0) {
                    safeCount++;
                }
            }
        }
        return safeCount;
    }
}

class Pos {
    int x, y;

    public Pos(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
