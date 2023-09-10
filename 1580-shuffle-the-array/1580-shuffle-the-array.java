class Solution {
    public int[] shuffle(int[] nums, int n) {
        int[] finalArray = new int[nums.length];
        int m = 0;

        for(int i = 0; i < nums.length; i++) {
            if (i % 2 == 0) {
                finalArray[i] = nums[m];
                m++;
            } else {
                finalArray[i] = nums[n];
                n++;
            }
        }

        return finalArray;
    }
}






