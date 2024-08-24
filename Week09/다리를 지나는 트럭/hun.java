import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time=0;

        Queue<Integer> bridge = new ArrayDeque<>();
        //타기 직전의 트럭 인덱스
        int startIdx = 0;
        //다리에 있는 차 무게총합
        int bridgeWeight = 0;

        for (int i = 0; i <bridge_length; i++) {
            bridge.add(0);
        }
        while (startIdx<truck_weights.length){
            bridgeWeight-= bridge.poll();

            int nextTruck = truck_weights[startIdx];
            if(bridgeWeight+nextTruck <= weight){
                bridge.add(nextTruck);
                bridgeWeight+= nextTruck;
                startIdx++;
            }else {
                bridge.add(0);
            }
            time++;
        }

        return time+bridge_length;
    }
}
