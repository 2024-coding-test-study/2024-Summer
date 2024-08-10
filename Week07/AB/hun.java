import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        long a = Long.parseLong(input[0]);
        long b = Long.parseLong(input[1]);
        int operations = 0;

        while (b > a) {
            if (b % 10 == 1) {
                b /= 10;  // 마지막 자리가 1이면 제거
            } else if (b % 2 == 0) {
                b /= 2;   // 짝수면 2로 나눈다
            } else {
                break;    // 그 외의 경우에는 더 이상 진행 불가
            }
            operations++;
        }

        if (b == a) {
            System.out.println(operations + 1);  // 변환 가능: 연산 횟수 + 1 출력
        } else {
            System.out.println(-1);  // 변환 불가능
        }
    }
}


//메모리 초과 실패,  홀수이거나 짝수이거나 둘 중 하나의 방법밖에 없다는 사실을 망각함
/*
class Main{
    public static int[] count;
    public static int a;
    public static int b;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] ab = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        a = ab[0];
        b = ab[1];

        count = new int[b-a];
        Arrays.fill(count,Integer.MAX_VALUE);

        fillCount(b-a-1, 0);

        if(count[0] ==0) System.out.println(-1);
        else System.out.println(count[0]);
    }
    public static void fillCount(int currentIdx, int currentCount){
        int nowB = a + currentIdx+1;
        //idx가 0이하면 종료
        if(currentIdx<0){
            return;
        }
        //연산한 값이 기존에 연산한 값보다 크거나 같으면 종료
        if(currentCount>=count[currentIdx]){
            return;
        }
        //리스트에 횟수삽입
        count[currentIdx] = currentCount;
        //연산 가능하다면 호출
        if((nowB-1)%10==0){
            fillCount((nowB-1)/10 -a-1,currentCount+1);
        }
        if(nowB%2!=0){
            fillCount(nowB/2 -a-1,currentCount+1);
        }
        return;
    }
}
*/