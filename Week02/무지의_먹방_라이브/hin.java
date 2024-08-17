//시간초과실패
import java.util.LinkedList;
class Solution {
    public static LinkedList<Integer> convertArrayToLinkedList(int[] array) {
        LinkedList<Integer> linkedList = new LinkedList<>();
        for (int num : array) {
            linkedList.add(num);
        }
        return linkedList;
    }
    public int solution(int[] food_times, long k) {
        LinkedList<Integer> linkedList = convertArrayToLinkedList(food_times);

        int foodIdx = 0;
        for(int i =0;i<k;i++){
            if(foodIdx>=linkedList.size()){
                foodIdx=0;
            }if(linkedList.size()==0){
                return -1;
            }if(linkedList.get(foodIdx)!=0){
                linkedList.set(foodIdx,linkedList.get(foodIdx)-1);
                foodIdx++;
            }else{
                linkedList.remove(foodIdx);
            }
        }
        return foodIdx;
    }
}