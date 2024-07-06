import java.io.*;
import java.util.Arrays;

public class Main {

    public static int binarySearch(int[] array, int target, int start, int end) {
        while (start <= end) {
            int mid = (start + end) / 2;
            if (array[mid] == target) {
                return mid;
            }
            if (array[mid] < target) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // N을 입력 받고 배열 초기화
        int N = Integer.parseInt(br.readLine());
        int[] NArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        // M을 입력 받고 배열 초기화
        int M = Integer.parseInt(br.readLine());
        int[] MArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        // 정렬 필요
        Arrays.sort(NArray);

        // 타임스탬프 추가
        long startTime = System.nanoTime();

        for (int target : MArray) {
            int result = binarySearch(NArray, target, 0, NArray.length - 1);
            if (result != -1) {
                bw.write("yes\n");
            } else {
                bw.write("no\n");
            }
        }

        long endTime = System.nanoTime();
        long duration = (endTime - startTime);

        bw.write("Elapsed time: " + duration + " nanoseconds\n");

        bw.flush();
        bw.close();
        br.close();
    }
}
