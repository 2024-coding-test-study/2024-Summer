    import java.util.*;

    class Solution {
        public static int[][] pillarMap;//0:비어있음, 1: 있음;
        public static int[][] boMap;//0:비어있음, 1: 있음;
        public static int n;

        public static int checkPillarIdx(int x, int y) {
            if (x < 0 || y < 0 || x > n || y > n-1) {
                return 0;
            }
            return 1;
        }

        public static int checkBoIdx(int x, int y) {
            if (x < 0 || y < 1 || x > n-1 || y > n) {
                return 0;
            }
            return 1;
        }

        public static int isPillar(int x, int y) {
            if (checkPillarIdx(x, y) == 1 && pillarMap[x][y] == 1) {
                return 1;
            }
            return 0;
        }

        public static int isBo(int x, int y) {
            if (checkBoIdx(x, y) == 1 && boMap[x][y] == 1) {
                return 1;
            }
            return 0;
        }

        public static int canPillar(int x, int y) {
            if (y == 0 || isPillar(x, y - 1) == 1 || isBo(x - 1, y) == 1 || isBo(x, y) == 1) {
                return 1;//조건 1에 해당
            }
            return 0;

        }

        public static int canBo(int x, int y) {
            if (isPillar(x, y - 1) == 1 || isPillar(x + 1, y - 1) == 1 || (isBo(x - 1, y) == 1 && isBo(x + 1, y) == 1)) {
                return 1;//조건 2에 해당
            }
            return 0;
        }

        public static int buildPillar(int x, int y) {
            if (canPillar(x, y) == 1) {
                pillarMap[x][y] = 1;
                return 1;
            }
            return 0;
        }

        public static int breakPillar(int x, int y) {
            pillarMap[x][y] = 0;
            if ((isBo(x, y + 1) == 1 && canBo(x, y + 1) == 0)||
                (isBo(x - 1, y + 1) == 1 && canBo(x - 1, y + 1) == 0)||
                (isPillar(x, y + 1) == 1 && canPillar(x, y + 1) == 0)) {
                    pillarMap[x][y] = 1;
                    return 0;
            }
            return 1;
        }

        public static int buildBo(int x, int y) {
            if (canBo(x, y) == 1) {
                boMap[x][y] = 1;
                return 1;
            }
            return 0;
        }

        public static int breakBo(int x, int y) {
            boMap[x][y] = 0;
            if((isBo(x + 1, y) == 1 && canBo(x + 1, y) == 0)||
                (isBo(x - 1, y) == 1 && canBo(x - 1, y) == 0)||
                (isPillar(x, y) == 1 && canPillar(x, y) == 0)||
                (isPillar(x + 1, y) == 1 && canPillar(x + 1, y) == 0)) {
                    boMap[x][y] = 1;
                    return 0;
            }
            return 1;
        }

        public static int findRemoveIdx(int a, int b, int c, List<int[]> list) {
            for (int i = 0; i < list.size(); i++) {
                int[] entity = list.get(i);
                if (entity[0] == a && entity[1] == b && entity[2] == c) {
                    return i;
                }
            }return -1;
        }
        public List<int[]> solution(int n, int[][] build_frame) {
            List<int[]> resultList = new LinkedList<>();
            Map<String,Integer> map = new HashMap<>();
            this.n = n;
            this.pillarMap = new int[n+1][n+1];
            this.boMap = new int[n+1][n+1];

            for(int[] input: build_frame){

                if(input[2]==0&&checkPillarIdx(input[0],input[1])==1){//기둥
                    if(input[3]==0){//부수다
                        if(breakPillar(input[0],input[1])==1){
                            int deleteIdx = findRemoveIdx(input[0],input[1],input[2],resultList);
                            resultList.remove(deleteIdx);
                        }
                    }else if(input[3]==1){//만들다
                        if(buildPillar(input[0],input[1])==1){
                            resultList.add(new int[]{input[0],input[1],input[2]});
                        }
                    }
                }else if(input[2]==1&&checkBoIdx(input[0],input[1])==1){//보
                    if(input[3]==0){//부수다
                        if(breakBo(input[0],input[1])==1){
                            int deleteIdx = findRemoveIdx(input[0],input[1],input[2],resultList);
                            resultList.remove(deleteIdx);
                        }
                    }else if(input[3]==1){//만들다
                        if(buildBo(input[0],input[1])==1){
                            resultList.add(new int[]{input[0],input[1],input[2]});
                        }
                    }
                }
            }
            //정렬방법이 잘못됐었음
//            resultList.sort((o1, o2) -> {
//                if (o1[0] == o2[0]) {
//                    return Integer.compare(o1[1], o2[1]);
//                }
//                return Integer.compare(o1[0], o2[0]);
//            });
            resultList.sort((o1, o2) -> {
                // 첫 번째 정수를 비교합니다.
                if (o1[0] == o2[0]) {
                    // 첫 번째 정수가 같다면 두 번째 정수를 비교합니다.
                    if (o1[1] == o2[1]) {
                        // 첫 번째와 두 번째 정수가 같다면 세 번째 정수를 비교합니다.
                        return Integer.compare(o1[2], o2[2]);
                    }
                    // 첫 번째 정수는 같고 두 번째 정수는 다르다면 두 번째 정수를 기준으로 정렬합니다.
                    return Integer.compare(o1[1], o2[1]);
                }
                // 첫 번째 정수가 다르다면 첫 번째 정수를 기준으로 정렬합니다.
                return Integer.compare(o1[0], o2[0]);
            });
            return resultList;
        }
    }
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[][] build_frame ={{1,0,0,1},{1,1,1,1},{2,1,0,1},{2,2,1,1},{5,0,0,1},{5,1,0,1},{4,2,1,1},{3,2,1,1}};
        List<int[]> result = s.solution(5,build_frame);
        for(int[] re: result){
            Arrays.toString(re);
            System.out.print(Arrays.toString(re));
        }
    }
}