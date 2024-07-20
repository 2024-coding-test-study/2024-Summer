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

        for(int i =0;i<4;i++){
            for(int j = -key.length+1; j<lock.length; j++){
                for(int k = -key.length+1; k<lock.length; k++){
                    if(check(j,k, Key)){
                        return true;
                    }
                }
            }Key = turn(Key);
            //System.out.println(Key);
        }
        return false;
    }

    public static Map<Integer,List<Integer>> turn(Map<Integer,List<Integer>> key){
        Map<Integer,List<Integer>> ResultKey = new HashMap<>();
        for(int i =0;i<key.size();i++) {
            ResultKey.put(i,new ArrayList<>());
        }
        for(int i =0;i<key.size();i++){
            for(int idx: key.get(i)){
                ResultKey.get(idx).add(key.size()-1-i);
            }
        }
        //돌리는 과정에서 순서가 유지되지 않아서 큐에서 꺼낼때 순서가 안맞았음
        for(int i =0;i<key.size();i++){
            Collections.sort(ResultKey.get(i));
        }
        return ResultKey;
    }
    //public static
    public static boolean check(int X, int Y, Map<Integer,List<Integer>> key){
        //List<List<Integer>> LockTmp = new ArrayList<>(Lock);


        Queue<int[]> lockQue = new ArrayDeque<>();
        for(int i =0;i<Lock.size();i++){
            for(int idx: Lock.get(i)){
                lockQue.add(new int[]{i,idx});
            }
        }

        Queue<int[]> keyQue = new ArrayDeque<>();
        for (int i = 0; i < key.size(); i++) {
            for (int idx : key.get(i)) {
                //Lock의 사이즈로 비교하지 않고 key.size()로 비교해서 틀렸었음
                if (i + X >= 0 && i + X < Lock.size() && idx + Y >= 0 && idx + Y < Lock.size()) {
                    keyQue.add(new int[]{i + X, idx + Y});
                }
            }
        }

        while (!lockQue.isEmpty()&&!keyQue.isEmpty()){
            int[] lockPoll = lockQue.poll();
            int[] keyPoll = keyQue.poll();
            if(lockPoll[0]!=keyPoll[0]||lockPoll[1]!=keyPoll[1]){
                return false;
            }
        }
        if(lockQue.isEmpty()&&keyQue.isEmpty()){
            return true;
        }return false;

    }

}