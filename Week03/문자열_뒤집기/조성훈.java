import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int[] s = Arrays.stream(br.readLine().split(""))
//                .mapToInt(Integer::parseInt)
//                .toArray();

        String s = br.readLine();
        int[] zeroOneCount = new int[2];
        int before = 100;
        for(int i =0; i<s.length;i++){
            if(before!=s[i]){
                zeroOneCount[s[i]] +=1;
                before=s[i];
            }
        }
        int result = zeroOneCount[0]<zeroOneCount[1]?zeroOneCount[0]:zeroOneCount[1];
        System.out.println(result);
        br.close();
    }
}
