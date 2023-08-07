class Solution {
    public int removeDuplicates(int[] nums) {
        int start = 1;
        int counter = 1;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i] != nums[i - 1]) {
                nums[start] = nums[i];
                start++;
                counter = 1;
            } else {
                if(counter < 2) {
                    nums[start] = nums[i];
                    start++;
                    counter++;
                }
            }
        }

        return start;
    }
}