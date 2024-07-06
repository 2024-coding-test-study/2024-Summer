package 모험가_길드;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class hun {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] list1 = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        Arrays.sort(list1);
        int now=list1[0];
        int count=0;
        int group=0;
        for(int i=0;i<list1.length;i++){
            if(list1[i]==now){
                count++;
            }else{
                group= count/list1[i-1];
                count=0;
            }
        }
    }

}
