import java.util.*;

class Solution {
    public static int[] Dist;
    public static int N;
    public static int minFriend = Integer.MAX_VALUE;

    public static void removeWeak(List<Integer> weak, int frendIdx) {
        if (weak.size() <= 0) { // 취약조건을 다 보수한 경우
            minFriend = Math.min(frendIdx, minFriend);
            return;
        }
        if (frendIdx >= minFriend || frendIdx >= Dist.length) { // 최솟값보다 커진 경우, 친구를 다 사용한 경우
            return;
        }

        for (int i = 0; i < weak.size(); i++) {
            List<Integer> tempWeak = new ArrayList<>(weak); // weak 복사
            int start = tempWeak.get(i);
            int weakIdx = i;
            // 친구가 보수한 부분 삭제
            while (weakIdx < tempWeak.size() && start + Dist[frendIdx] >= tempWeak.get(weakIdx)) { // 현재 친구가 지운 마지막값이 취약점 숫자보다 크면
                tempWeak.remove(weakIdx);
            }
            if (start + Dist[frendIdx] >= N) { // 한바퀴 돌았다면
                weakIdx = 0;
                while (weakIdx < tempWeak.size() && start + Dist[frendIdx] - N >= tempWeak.get(weakIdx)) {
                    tempWeak.remove(weakIdx);
                }
            }
            removeWeak(tempWeak, frendIdx + 1);
        }
    }

    public int solution(int n, int[] weak, int[] dist) {
        N = n;
        Dist = sortDesc(dist);
        List<Integer> newWeak = new ArrayList<>();
        for (int w : weak) {
            newWeak.add(w);
        }
        removeWeak(newWeak, 0);
        return minFriend == Integer.MAX_VALUE ? -1 : minFriend; // 만약 모든 친구를 사용해도 불가능한 경우 -1 반환
    }

    public static int[] sortDesc(int[] array) {
        Integer[] list = Arrays.stream(array).boxed().toArray(Integer[]::new);
        Arrays.sort(list, Collections.reverseOrder());
        return Arrays.stream(list).mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int n = 12;
        int[] weak = {1, 5, 6, 10};
        int[] dist = {1, 2, 3, 4};

        int result = sol.solution(n, weak, dist);
        System.out.println("Result: " + result); // Expected output: 2
    }
}
