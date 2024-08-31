import java.util.*;

class Solution {
        public int solution(String[][] book_time) {
        List<int[]> time = new LinkedList<>();

        for (int i = 0; i < book_time.length; i++) {
            int[] timeEntity = new int[2];
            for (int j = 0; j < 2; j++) {
                int[] tmp = Arrays.stream(book_time[i][j].split(":")).mapToInt(Integer::parseInt).toArray();
                timeEntity[j] = tmp[0]*60 + tmp[1];
                if(j==1) timeEntity[j]+=10;
            }
            time.add(timeEntity);
        }
        time.sort((o1, o2) -> {//시작시간을 기준으로 정렬해야함
            if (o1[0] == o2[0]) {
                return o1[1] - o2[1]; 
            }
            return o1[0] - o2[0];
        });
        int roomCount = 0;
        while (!time.isEmpty()){
            int lastTime=0;
            int i=0;
            while (i<time.size()){
                if (lastTime<=time.get(i)[0]){
                    lastTime = time.remove(i)[1];
                }else i++;
            }roomCount++;
        }
        return roomCount;

    }
}
