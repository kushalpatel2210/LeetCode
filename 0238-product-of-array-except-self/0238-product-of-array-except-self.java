class Solution {
    public int[] productExceptSelf(int[] nums) {
        int N = nums.length;
        int[] left_product = new int[N];
        int[] right_product = new int[N];
        int[] product = new int[N];
        int leftProduct = 1;
        int rightProduct = 1;

        for (int i = 0; i < N; i++) {
            if (i <= 0) {
                left_product[i] = 1;
            } else {
                leftProduct *= nums[i-1];
                left_product[i] = leftProduct;
            }
        }

        for (int i = N -1; i >= 0; i--) {
            if (i >= N -1) {
                right_product[i] = 1;
            } else {
                rightProduct *= nums[i+1];
                right_product[i] = rightProduct;
            }
            product[i] = left_product[i] * right_product[i];
        }
        return product;
    }
}