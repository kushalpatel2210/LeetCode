class Solution {
    public String reverseVowels(String s) {
        boolean[] isVowel = new boolean[128];
        int left = 0; 
        int right = s.length() - 1;
        char[] charArray = s.toCharArray();
        
        for (char c : "aeiouAEIOU".toCharArray()) {
            isVowel[c] = true;
        }

        while (left < right) {

            while (left < right && !isVowel[charArray[left]]) {
                left++;
            } 
            
            while (left < right && !isVowel[charArray[right]]) {
                right--;
            }
            
            if (left < right) {
                char temp = charArray[left];
                charArray[left] = charArray[right];
                charArray[right] = temp;
                left++;
                right--;
            } 
        }
        return String.valueOf(charArray);
    }
}