import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Map<Character, Integer> alphabetMap = new HashMap<>();
        String[] sList = new String[n];

        // 각 단어 입력 및 가중치 계산
        for(int i = 0; i < n; i++){
            String s = br.readLine();
            sList[i] = s;
            int len = s.length();
            for(int j = 0; j < len; j++){
                char c = s.charAt(j);
                int weight = (int) Math.pow(10, len - j - 1);
                alphabetMap.put(c, alphabetMap.getOrDefault(c, 0) + weight);
                //map.getOrDefault(c, 0)    -> 쓸일 많을 듯
            }
        }
        // 값 기준 내림차순 정렬 1
//        List<Character> keySet = new ArrayList<>(alphabetMap.keySet());
//        keySet.sort(new Comparator<Character>() {
//            @Override
//            public int compare(Character o1, Character o2) {
//                return alphabetMap.get(o2).compareTo(alphabetMap.get(o1)); // 내림차순
//            }
//        });


        // 값 기준 내림차순 정렬 2
        List<Map.Entry<Character, Integer>> entryList = new ArrayList<>(alphabetMap.entrySet());
        entryList.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        // 9부터 숫자 배정
        int number = 9;
        Map<Character, Integer> charToDigit = new HashMap<>();
        for (Map.Entry<Character, Integer> entry : entryList) {
            charToDigit.put(entry.getKey(), number--);
        }

        // 각 단어를 숫자로 변환하여 합산
        int result = 0;
        for (String word : sList) {
            int num = 0;
            for (int j = 0; j < word.length(); j++) {
                num = num * 10 + charToDigit.get(word.charAt(j));
            }
            result += num;
        }
        System.out.println(result);
    }
}
