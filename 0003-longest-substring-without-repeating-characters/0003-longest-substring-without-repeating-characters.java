class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();        
        int left = 0, right = 0;
        int longestSubstringLength = Integer.MIN_VALUE;

        while (right < s.length()) {
            char currentChar = s.charAt(right);

            if (!set.contains(currentChar)) {
                set.add(currentChar);
                right++;
                longestSubstringLength = Math.max(longestSubstringLength, set.size());
            } else {
                set.remove(s.charAt(left));
                left++; 
            }
        }
        
        return longestSubstringLength < 0 ? 0 : longestSubstringLength;
    }
}