class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] contatenatedArray = new int[2*n];

        for(int i = 0; i < n; i++) {
            contatenatedArray[i] = nums[i];
            contatenatedArray[i+n] = nums[i];
        }

        return contatenatedArray;
    }
}