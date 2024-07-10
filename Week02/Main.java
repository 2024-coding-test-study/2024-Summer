import java.io.*;
import java.util.*;

/*
public class Main {
    public int ground(int n, int[] nList){
        if(n==1){
            return 1;
        }else if(n==2){
            return 3;
        }
        else if(n>2){
            if(nList[n-1] == 0){
                nList[n-1] = ground(n-1, nList);

            }if(nList[n-2] == 0){
                nList[n-2] = ground(n-2, nList);

            }
            return (nList[n-1]+nList[n-2]*2)%796797;
        }
        else return 0;
    }
    public static void main(String[] args) throws IOException {
        int[] nList = new int[796797];
        nList[0] = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Main m = new Main();

        int result = m.ground(n,nList);
        System.out.println(result);
    }
}
/*

public class Main{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int[] NM = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

    List<int[]> graph = new ArrayList<>();
    for(int i =0;i<NM[0];i++){
        row = Arrays.stream(br.readLine().split())
                .mapToInt(Integer::parseInt)
                .toArray();
        graph.append(row);
    }

    public static int dfs(int x, int y){
        if(x<0 || x>NM[0] || y<0 || y>NM[1]){
            return 0;
        }if(graph[x][y]==0){
            graph[x][y] =1;
            dfs(x+1,y);
            dfs(x-1,y);
            dfs(x,y+1);
            dfs(x,y-1);
            return 1;
        }else{
            return 0;
        }
    }
    int result = 0;
    for(int i =0;i<NM[0];i++){
        for(int j=0; j<NM[1];j++){
            if(graph[i][j] == 0){
                dfs(i,j);
                result++;
            }
        }
    }System.out.println(result);

    bw.close();
    br.close();


} */


public class Main{

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int[] NM = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

    List<int[]> graph = new ArrayList<>();
    for(int i =0;i<NM[0];i++){
        int[] row = Arrays.stream(br.readLine().split())
                .mapToInt(Integer::parseInt)
                .toArray();
        graph.append(row);
    }

    public static int dfs(int x, int y){
        if(x<0 || x>NM[0] || y<0 || y>NM[1]){
            return 0;
        }if(graph[x][y]==0){
            graph[x][y] =1;
            dfs(x+1,y);
            dfs(x-1,y);
            dfs(x,y+1);
            dfs(x,y-1);
            return 1;
        }else{
            return 0;
        }
    }

    public static void main(String[] args) throws IOException {

        int result = 0;
        for(int i =0;i<NM[0];i++){
            for(int j=0; j<NM[1];j++){
                if(graph[i][j] == 0){
                    dfs(i,j);
                    result++;
                }
            }
        }System.out.println(result);

        bw.close();
        br.close();
    }



}