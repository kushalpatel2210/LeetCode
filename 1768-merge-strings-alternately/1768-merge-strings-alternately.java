class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder mergedString = new StringBuilder();
        int word1Length = word1.length();
        int word2Length = word2.length();

        for (int i = 0; i < word1Length; i++) {
            if (i == word2Length) {
                mergedString.append(word1.substring(i, word1Length));
                break;
            }
            mergedString.append(word1.charAt(i));
            mergedString.append(word2.charAt(i));
        }
        
        if (word2Length > word1Length) {
            mergedString.append(word2.substring(word1Length, word2Length));
        }

        return mergedString.toString();
    }
}