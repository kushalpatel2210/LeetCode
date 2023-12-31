class Solution {
    public void moveZeroes(int[] nums) {
        int N = nums.length;
        int start = 0;
        for (int i = 0; i < N; i++) {
            if (nums[i] != 0) {
                nums[start++] = nums[i];
            }
        }

        while (start < N) {
            nums[start++] = 0; 
        }
    }
}
 
/* 
-----------------Runtime High Solution--------------------
class Solution {
    public void moveZeroes(int[] nums) {
        int N = nums.length;
        for (int i = 0; i < N; i++) {
            int curr = nums[i];

            if (curr == 0) {
                int nextIndex = i + 1;
                while (nextIndex < N && nums[nextIndex] == 0) {
                    nextIndex++;
                }

                if (nextIndex < N) {
                    nums[i] = nums[nextIndex];
                    nums[nextIndex] = curr;
                }    
            }
        }
    }
}
*/