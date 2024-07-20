import javax.print.DocFlavor;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int n;
    public static Queue<Integer> queue = new ArrayDeque<>();
    public static List<List<Integer>> course = new ArrayList<>();
    public static int[] toStudyCourse;
    public static int[] time;
    public static void topologySort(){
        int[] result = new int[n];
        for(int i=0;i<n;i++){
            if (toStudyCourse[i]==0){
                queue.add(i);
            } result[i] = time[i];
        }
        while (!queue.isEmpty()) {
            int currentQueue = queue.poll();
            for(int i : course.get(currentQueue)){
                result[i] = Math.max(result[i], result[currentQueue]+time[i]);
                toStudyCourse[i]--;
                if(toStudyCourse[i]==0){
                    queue.add(i);
                }

            }
        }for(int i : result){
            System.out.println(i);
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        toStudyCourse = new int[n];
        time = new int[n];
        for(int i =0;i<n;i++){
            course.add(new ArrayList<Integer>());
        }

        for(int i =0;i<n;i++){
            int[] input = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            time[i] = input[0];
            for(int j =1;j<input.length-1;j++){
                course.get(input[j]-1).add(i);
                toStudyCourse[i]++;
            }

        }topologySort();

    }
}
//아래와같은 재귀적 방식으로 풀려했으나 실패 반복문으로 해야할듯
//public static int topologySort(Queue<Integer> queue, List<int[]> course, List<Integer> toStudyCourse){
//    int currentQueue = queue.peek();
//    for(int i =0;i<toStudyCourse.toArray().length;i++){
//        for(int j=1;j<course.get(i).length-1;j++){
//            if(course.get(i)[j]==currentQueue+1){
//                toStudyCourse.set(i,toStudyCourse.get(i)-1);
//            }
//        }
//    }
//    for(int i=0;i<toStudyCourse.toArray().length;i++){
//        if (toStudyCourse.get(i)==0){
//            queue.add(i);
//        }
//    }
//    int result = course.get(currentQueue)[0];
//    if(!queue.isEmpty()){
//        return result + topologySort(queue,course,toStudyCourse);
//    }else{
//        return result;
//    }
//}