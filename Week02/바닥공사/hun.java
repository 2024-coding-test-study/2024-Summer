package 바닥공사;

public class hun {
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
}
/*
import java.io.*;

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

 */