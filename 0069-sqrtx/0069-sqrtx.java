class Solution {
    public int mySqrt(int x) {
        long result = 1;
        long temp = 0;
        if (x==0){
            return 0;
        }
        for(long i=1; i<=x/2; i++){
            temp = i*i;
            if (temp>x){
                break;
            }
            if (temp<=x){
                result = i;
            }
        }
        return (int) result;
    }
}