import java.util.*;
class Solution {
    public static Map<Integer,List<Integer>> Key = new HashMap<>();
    public static List<List<Integer>> Lock = new ArrayList<>();
    public static Map<Integer,List<Integer>> ResultKey = new HashMap<>();
    public boolean solution(int[][] key, int[][] lock) {


        for(int i =0;i<key.length;i++) {
            Key.put(i,new ArrayList<>());
        }
        for(int i =0;i<key.length;i++){
            for(int j =0;j<key.length;j++){
                if(key[i][j]==1){
                    Key.get(i).add(j);
                }
            }
        }
        for(int i =0;i<lock.length;i++) {
            Lock.add(new ArrayList<>());
        }
        for(int i =0;i<lock.length;i++){
            for(int j =0;j<lock.length;j++){
                if(lock[i][j]==0){
                    Lock.get(i).add(j);
                }
            }
        }

        boolean answer = true;
        return answer;
    }
    public static void turn(List<List<Integer>> key){
        for(int i =0;i<key.size();i++) {
            ResultKey.put(i,new ArrayList<>());
        }
        for(int i =0;i<key.size();i++){
            for(int idx: key.get(i)){
                ResultKey.get(idx).add(key.size()-1-i);
            }
        }return;
    }
    public static boolean check(){
        //List<List<Integer>> LockTmp = new ArrayList<>(Lock);
        Queue<int[]> lockQue = new ArrayDeque<>();
        for(int i =0;i<Lock.size();i++){
            for(int idx: Lock.get(i)){
                lockQue.add(new int[]{i,idx});
            }
        }
        Queue<int[]> keyQue = new ArrayDeque<>();
        for(int i =0;i<Key.size();i++){
            for(int idx: Key.get(i)){
                keyQue.add(new int[]{i,idx});
            }
        }
        while ()
            for(int i =0;i<Lock.size();i++){
                for(int idx: Lock.get(i)){
                    LockTmp.get
                }
            }
    }

}