import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int cnt = 0;
    public static int[][] map;
    public static int lIdx = 0;
    public static String[][] turnIdx;
    public static int currentWay = 1; // 처음에 오른쪽으로 이동
    public static int[] currentIdx = {0, 0};
    public static int[] endIdx = {0, 0};
    public static Deque<int[]> snake = new ArrayDeque<>(); // 뱀의 몸을 큐로 관리

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[][] appleIdx = new int[k][2];
        for (int i = 0; i < k; i++) {
            appleIdx[i] = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }
        int l = Integer.parseInt(br.readLine());
        turnIdx = new String[l][2];
        for (int i = 0; i < l; i++) {
            turnIdx[i] = br.readLine().split(" ");
        }
        map = new int[n][n];
        for (int[] a : appleIdx) {
            map[a[0] - 1][a[1] - 1] = 1; // 사과가 있는 자리는 1
        }
        snake.add(new int[]{0, 0});
        map[0][0] = 2; // 뱀이 있는 자리는 2

        while (true) {
            cnt++;
            if (!move()) {
                break;
            }
            if (lIdx < turnIdx.length && cnt == Integer.parseInt(turnIdx[lIdx][0])) {
                turn(turnIdx[lIdx][1]);
                lIdx++;
            }
        }
        System.out.println(cnt);
    }

    public static boolean move() {
        int[] nextIdx = moveNode(currentIdx, currentWay);

        if (nextIdx[0] < 0 || nextIdx[0] >= map.length || nextIdx[1] < 0 || nextIdx[1] >= map.length || map[nextIdx[0]][nextIdx[1]] == 2) {
            return false; // 벽이나 자기 자신과 부딪히면 게임 종료
        }

        if (map[nextIdx[0]][nextIdx[1]] != 1) { // 사과가 없다면
            int[] tail = snake.pollLast();
            map[tail[0]][tail[1]] = 0; // 꼬리를 움직임
        }

        snake.addFirst(nextIdx);
        map[nextIdx[0]][nextIdx[1]] = 2;
        currentIdx = nextIdx;
        return true;
    }

    public static int[] moveNode(int[] node, int way) {
        int[] newNode = Arrays.copyOf(node, 2);
        if (way == 1) {
            newNode[1] += 1; // 오른쪽
        } else if (way == -1) {
            newNode[1] -= 1; // 왼쪽
        } else if (way == -2) {
            newNode[0] -= 1; // 위
        } else if (way == 2) {
            newNode[0] += 1; // 아래
        }
        return newNode;
    }

    public static void turn(String direction) {
        if (direction.equals("L")) {
            currentWay = currentWay == 1 ? -2 : currentWay == -2 ? -1 : currentWay == -1 ? 2 : 1;
        } else {
            currentWay = currentWay == 1 ? 2 : currentWay == 2 ? -1 : currentWay == -1 ? -2 : 1;
        }
    }
}
