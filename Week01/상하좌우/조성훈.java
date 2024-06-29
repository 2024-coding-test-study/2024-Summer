
public class Greedy{

    public int lawOfLargeNumber(int[] numList, int k, int m){
        int large1 = numList[0];
        int large2 = 0;
        for(int i = 1;i<numList.length;i++){
            if(large1<numList[i]){
                large1 = numList[i];
            } else if (large1==numList[i]) {
                large2 = numList[i]
            }
            if(large2<numList[i]&&){
                large2 = numList[i];
            }
        }
    }
    public static void main(String[] args) {

    }
}