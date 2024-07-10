import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] member = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        Arrays.sort(member);
        int before = member[0];
        int countEqualLevel = 0;
        int result = 0;
        for(int i =0;i<member.length;i++){
            if(before==member[i]){
                countEqualLevel++;
            }else{
                result += countEqualLevel/before;
                int nextIdx = i+ before- countEqualLevel%before;
                if(countEqualLevel%before!=0&member.length>nextIdx){
                    i = nextIdx;
                }
                before = member[i];
            }

        }System.out.println(result);
        br.close();
    }
}