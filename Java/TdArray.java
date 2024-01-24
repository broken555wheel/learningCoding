public class TdArray {
    public static void main(String[] args) {
        int[][] tdArray = {{10,9,8,7,6,5,4,3,2,1},{11,12,13,14,15,16,17,18,19,20}};
        int sum =0;
        for (int i=0;i<tdArray.length;i++){
            for (int j=0;j<tdArray[i].length;j++){
                sum+=tdArray[i][j];
            }
        }
        System.out.println(sum);
    }
}
