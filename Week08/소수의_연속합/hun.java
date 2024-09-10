import java.io.*;
import java.util.*;

public class Main {
    // 소수의 합
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Integer> list = makePrimeList(n);

        int start = 0;
        int end = 0;
        int sum = 0;
        int result = 0;

        while (end < list.size()) {
            sum += list.get(end++);
            // 조건에 만족하는 최솟값, start<end의 조건을 만족함
            while (sum > n && start < end) {
                sum -= list.get(start++);
            }
            if (sum == n) {
                result++;
            }
        }
        System.out.println(result);
    }

    // n 이하의 소수 리스트를 반환
    public static List<Integer> makePrimeList(int num) {
        List<Integer> list = new ArrayList<>();
        if (num < 2) return list; // 2보다 작은 수는 소수가 없음

        // 소수 여부를 확인하기 위한 boolean 배열
        boolean[] isPrime = new boolean[num + 1];
        Arrays.fill(isPrime, true); // 모든 숫자를 소수로 가정
        isPrime[0] = isPrime[1] = false; // 0과 1은 소수가 아님

        // 에라토스테네스의 체 알고리즘
        // 소수로 표기되어있다면 해당 단위에서 기존에 탐색한 i까지는 이미 탐색을 완료했던 것임
        // 따라서 i*i + 1, 2,....와 같이 탐색하지 않은 값들부터 탐색을 시작함
        //ex) i==6  ->   6*6 ,  6*7 , 6*8 ...
        for (int i = 2; i * i <= num; i++) {
            if (isPrime[i]) {
                for (int multiple = i * i; multiple <= num; multiple += i) {
                    isPrime[multiple] = false;
                }
            }
        }

        // 소수 리스트 생성
        for (int i = 2; i <= num; i++) {
            if (isPrime[i]) {
                list.add(i);
            }
        }

        return list;
    }
}
