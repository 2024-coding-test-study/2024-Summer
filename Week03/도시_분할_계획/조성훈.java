import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static int findParent(int[] parent, int x){
        if(parent[x]!=x){
            parent[x]=findParent(parent,parent[x]);
        }return parent[x];
    }
    public static void union(int[] parent, int a, int b){
        a = findParent(parent,a);
        b = findParent(parent,b);
        if(a<b){
            parent[b] = a;
        }else {
            parent[a] = b;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nm = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] parent = new int[nm[0]];
        for(int i =0;i<nm[0];i++){
            parent[i] = i;
        }
        //TreeMap을 사용해야하는지 고민했었음
        List<int[]> abcs = new ArrayList<>();

        for(int i =0;i<nm[1];i++){
            int[] abc = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            abcs.add(abc);
        }

        Collections.sort(abcs,new Comparator<int[]>(){
            @Override
            public int compare(int[] a, int[] b){
                return Integer.compare(a[2],b[2]);
            }
        });
        int result = 0;
        int lastHome = 0;
        for(int i =0;i<nm[1];i++){
            int a = abcs.get(i)[0]-1;
            int b = abcs.get(i)[1]-1;
            if(findParent(parent,a)!= findParent(parent,b)){
                union(parent,a,b);
                result += abcs.get(i)[2];
                lastHome = abcs.get(i)[2];
            }
        }
        System.out.println(result-lastHome);
        System.out.println(result+" "+lastHome);

    }
}