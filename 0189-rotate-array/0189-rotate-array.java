import java.util.*;

class Solution {
    public void rotate(int[] nums, int k) {
        k = k % nums.length;
        reverse(nums, 0, nums.length - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, nums.length - 1);
    }

    private void reverse(int[] nums, int startIndex, int endIndex) {
        int left = startIndex;
        int right = endIndex;

        while(left < right) {
            int temp = nums[left];
            nums[left] = nums[right];
            nums[right] = temp;
            left++;
            right--;
        }
    }
} 

/* 
------------------Solution 1------------------------
class Solution {
    public void rotate(int[] nums, int k) {
        while(k > 0) {
            int lastElement = nums[nums.length - 1];
            moveElementByOne(nums);
            nums[0] = lastElement;
            k--;
        }
    }

    private void moveElementByOne(int[] nums) {
        for(int i = nums.length - 1; i > 0; i --) {
            nums[i] = nums[i-1];
        }
    }
} 
*/

/*
------------------Solution 2--------------------------
class Solution {
    public void rotate(int[] nums, int k) {
        int breakpoint;
        int[] newArray = new int[nums.length];
        int start = 0;
        
        if (k <= nums.length) {
            breakpoint = nums.length - k;
        } else {
            breakpoint = nums.length - (k % nums.length);
        }

        for(int i = breakpoint; i < nums.length; i++) {
            newArray[start] = nums[i];
            start++;
        }   

        for(int i = 0; i < breakpoint; i ++) {
            newArray[start] = nums[i];
            start++;
        }

        for(int i = 0; i <nums.length; i++) {
            nums[i] = newArray[i];
        }
    }
} 
*/