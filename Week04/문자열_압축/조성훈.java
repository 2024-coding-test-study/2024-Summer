class Solution {
    public int solution(String s) {
        int minLength = s.length();

        for(int i=1;i<=s.length()/2;i++){
            int countEqualsAgain=0;//중첩된 횟수
            int reduce = 0;
            for(int j=0;j<s.length()-i-i+1;j+=i){
                int loofDone = 0;
                int toCheckEquals =0;
                //문자가 모두 일치하는지, k와 같으면 모두 일치 equals의 시간복잡도 줄이기 위함
                for(int k=0;k<i;k++){
                    if(s.charAt(j+k)==s.charAt((j+k+i))){
                        toCheckEquals++;
                    }else{break;}

                }if(i==toCheckEquals){
                    countEqualsAgain++;
                    if(j==s.length()-s.length()%i-2*i){//마지막에 맞는걸로 끝내니까 올리지 못하길래 추가함(마지막의 기준을 정확히 잡음)
                        if(countEqualsAgain>=999){
                            reduce += (i*countEqualsAgain -4); //줄인 값
                        }else if(countEqualsAgain>=99) {
                            reduce += (i*countEqualsAgain -3); //줄인 값
                        }else if(countEqualsAgain>=9){
                            reduce += (i*countEqualsAgain -2); //줄인 값
                        }else{
                            reduce += (i*countEqualsAgain -1); //줄인 값
                        }
                        countEqualsAgain=0;

                    }
                }else{
                    if(countEqualsAgain!=0){
                        if(countEqualsAgain>=999){
                            reduce += (i*countEqualsAgain -4); //줄인 값
                        }else if(countEqualsAgain>=99) {
                            reduce += (i*countEqualsAgain -3); //줄인 값
                        }else if(countEqualsAgain>=9){
                            reduce += (i*countEqualsAgain -2); //줄인 값
                        }else{
                            reduce += (i*countEqualsAgain -1); //줄인 값
                        }
                        countEqualsAgain=0;
                    }
                }
            }minLength = Math.min(minLength,s.length()-reduce);
        }
        return minLength;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Test cases
        String[] testCases = {"ababcdcdababcdcda", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"};

        for (String s : testCases) {
            int result = sol.solution(s);
            System.out.println("Compressed length of \"" + s + "\": " + result);
        }
    }
}