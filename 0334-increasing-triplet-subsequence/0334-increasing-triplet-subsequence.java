class Solution {
    public boolean increasingTriplet(int[] nums) {
        int minOne = Integer.MAX_VALUE;
        int minTwo = Integer.MAX_VALUE;

        for (int num: nums) {
            if (num <= minOne) {
                minOne = num;
            } else if (num <= minTwo) {
                minTwo = num;
            } else {
                return true;
            }
        }

        return false;
    }
}