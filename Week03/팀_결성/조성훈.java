import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static int findParent(int[] parent, int x){
        if(parent[x] != x){
            parent[x] = findParent(parent,parent[x]);
        }
        return parent[x];
    }
    public static void union(int[] parent, int a, int b){
        if(parent[a]<parent[b]){
            parent[b]=a;
        }else{
            parent[a]= b;
        }
    }
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] mn= Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int[] parent = new int[mn[1]];
        for (int i =0;i<mn[1];i++){
            parent[i]=i;
        }
        //mn[0]+1번 반복해야 첫 입력 받을 수 있다는거 깜빡함
        for(int i =0;i<mn[0]+1;i++){
            int[] input= Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            if(input[0]==0){
                union(parent, input[1], input[2]);
            }else if(input[0]==1){
                if(findParent(parent,input[1])==findParent(parent,input[2])){
                    System.out.println("YES");
                }else{
                    System.out.println("NO");
                }
            }
        }br.close();


    }
}