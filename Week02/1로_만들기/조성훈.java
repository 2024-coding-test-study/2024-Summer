import java.io.*;

public class 조성훈{
    public void makeOne(int n) {

        int[] array = new int[n];
        array[0] = 0;
        array[1] = 0;
        for(int i =2; i<n+1; i++){
            array[i] = array[i-1];
            if(i%5==0){
                if(array[i]>array[i/5])
                    array[i] = array[i/5];
            }if(i%3==0){
                if(array[i]>array[i/3])
                    array[i] = array[i/3];
            }if(i%2==0){
                if(array[i]>array[i/2])
                    array[i] = array[i/2];
            }
        }

        System.out.println(array[n]);
    }
}