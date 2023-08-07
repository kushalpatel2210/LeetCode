class Solution {
    public int[] productExceptSelf(int[] nums) {
        int N = nums.length;
        int[] product = new int[N];
        int[] leftProduct = new int[N];
        int[] rightProduct = new int[N];
        int right = N - 1;
        int left_product = 1;
        int right_product = 1;
        
        for(int i = 0; i < N; i++) {
            if(i <= 0) {
                leftProduct[i] = 1;
            } else {
                left_product *= nums[i-1]; 
                leftProduct[i] = left_product;
            }
        }
        
        for(int j = N - 1; j >= 0; j --){
            if(j >= N - 1){
                rightProduct[j] = 1;
            } else {
                right_product *= nums[j+1];
                rightProduct[j] = right_product;
            }
            product[j] = leftProduct[j] * rightProduct[j];
        }

        return product;
    }
}