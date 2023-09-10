class Solution {
    public int[] buildArray(int[] nums) {
        int[] permutationArray = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            permutationArray[i] = nums[nums[i]]; 
        }

        return permutationArray;
    }
}