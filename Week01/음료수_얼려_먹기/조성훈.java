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


}