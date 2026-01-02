import java.util.HashMap;

class Solution {
    public int repeatedNTimes(int[] nums) {
        HashMap<Integer, Integer> countNumber = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            if (countNumber.containsKey(nums[i])) {
                return nums[i]; 
            }

            countNumber.put(nums[i], 1);
        }
        return 0;
    }
}