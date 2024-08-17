import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int totalScore = 0;
        Stack<Assignment> scoreStack = new Stack<>();

        for (int i = 0; i < n; i++) {
            int[] input = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            if (input[0] == 1) {
                scoreStack.push(new Assignment(input[1], input[2]));
            }

            if (!scoreStack.isEmpty()) {
                Assignment current = scoreStack.peek();
                current.time -= 1;
                if (current.time == 0) {
                    totalScore += current.score;
                    scoreStack.pop();
                }
            }
        }

        System.out.println(totalScore);
    }
}

class Assignment {
    int score;
    int time;

    Assignment(int score, int time) {
        this.score = score;
        this.time = time;
    }
}
