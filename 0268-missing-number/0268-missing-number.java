class Solution {
    public int missingNumber(int[] nums) {
        int temp;
        for(int i=0; i<nums.length; i++){
            for(int j=0; j<nums.length; j++)
            {
                if (nums[i]<nums[j]){
                    temp = nums[i];
                    nums[i]=nums[j];
                    nums[j]=temp;
                }
            }
        }
        for(int i=0; i<nums.length; ++i){
            if (i!=nums[i]){
                return i;
            }
        }
        int answer= nums[nums.length-1]+1;
        return answer;
    }
}