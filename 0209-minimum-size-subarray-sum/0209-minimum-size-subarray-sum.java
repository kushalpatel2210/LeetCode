class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0, sum = 0;
        int minSubArraySize = Integer.MAX_VALUE;

        while (right < nums.length) {
            sum += nums[right++];

            while (sum >= target) {
                minSubArraySize = Math.min(minSubArraySize, right - left);
                sum -= nums[left++];
            }
        }

        return minSubArraySize > nums.length ? 0 : minSubArraySize;
    }
}