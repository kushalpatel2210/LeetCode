class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^A-Za-z0-9]","").toLowerCase();
        int left = 0;
        int right = s.length() - 1;
        boolean isPalindrome = true;
    
        while(left <= right){
            if(s.charAt(left) == s.charAt(right)){
                left++;
                right--;
            } else {
                isPalindrome = false;
                break;
            }
        }

        return isPalindrome;
    }
}