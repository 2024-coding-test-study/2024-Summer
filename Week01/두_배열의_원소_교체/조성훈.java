import java.io.*;
public class Main{
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // N을 입력 받고 배열 초기화
        int NK[] = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray);

        Integer.parseInt(br.readLine());
        int[] AArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        // M을 입력 받고 배열 초기화
        int[] BArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        Arrays.sort(NK);
        Arrays.sort(AArray);
        Arrays.sort(BArray);

        int temp = 0;
        for(int i =0;i<NK[1];i++){
            if(AArray[i] < BArray[NK[0]-i-1]){
                AArray[i] = BArray[NK[0]-i-1];
            }else{
                break;
            }
        }
        for(int i : AArray){
            result += i;
        }
        bw.write(result);
        bw.flush();
        bw.close();
        br.close();

    }
}