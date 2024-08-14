import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String s =br.readLine();
        boolean startWith = true;
        if(s.charAt(0) == '-') startWith = false;
        String[] sList =  s.split("-");
        int result =  Arrays.stream(sList[0].split("\\+"))
                .mapToInt(Integer::parseInt)
                .sum();
        if(!startWith) result*=-1;
        int sListLen = sList.length;
        if(sListLen==1){
            System.out.println(result);
            return;
        }
        for (int i = 1; i < sListLen; i++) {
            result -=  Arrays.stream(sList[i].split("\\+"))
                    .mapToInt(Integer::parseInt)
                    .sum();
        }
        bw.write(result + "\n");
        bw.flush();
    }
}