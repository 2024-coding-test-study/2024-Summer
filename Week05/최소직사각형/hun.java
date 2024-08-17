class Solution {
    public int solution(int[][] sizes) {
        int maxX = 0;
        int maxY = 0;
        for(int i = 0;i<sizes.length;i++){
            int big,small;
            if(sizes[i][0]>sizes[i][1]){
                big = sizes[i][0];
                small = sizes[i][1];
            }else{
                big = sizes[i][1];
                small = sizes[i][0];
            }
            if(maxX<big)maxX=big;
            if(maxY<small)maxY=small;
        }
        return maxX*maxY;
    }
}